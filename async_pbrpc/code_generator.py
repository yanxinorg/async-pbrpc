import typing

from google.protobuf.compiler import plugin_pb2  # type: ignore
from google.protobuf import descriptor_pb2  # type: ignore


_response = plugin_pb2.CodeGeneratorResponse()
_message_path_2_file_path: typing.Dict[str, str] = {}
_message_path_2_message_name_offset: typing.Dict[str, int] = {}
_package_name_counts: typing.Dict[str, int] = {}
_package_importations: typing.List[typing.Tuple[typing.Optional[str], str, str]] = []
_file_path_2_package_alias: typing.Dict[str, str] = {}


def generate_code(request: plugin_pb2.CodeGeneratorRequest) -> plugin_pb2.CodeGeneratorResponse:
    global _response

    if len(request.proto_file) == 0:
        return

    for fd in request.proto_file:
        _process_file1(fd)

    for fd in request.proto_file:
        _process_file2(fd)

    response = _response
    _response = plugin_pb2.CodeGeneratorResponse()
    _message_path_2_file_path.clear()
    _message_path_2_message_name_offset.clear()
    return response


def _process_file1(fd: descriptor_pb2.FileDescriptorProto) -> None:
    if len(fd.message_type) == 0:
        return

    message_path_prefix = "."

    if fd.package != "":
        message_path_prefix += fd.package + "."

    message_name_offset = len(message_path_prefix)
    file_path = fd.name

    for md in fd.message_type:
        _process_message(md, message_path_prefix, message_name_offset, file_path)


def _process_message(md: descriptor_pb2.DescriptorProto, message_path_prefix: str
                     , message_name_offset: int, file_path: str) -> None:
    message_path = message_path_prefix + md.name
    _message_path_2_file_path[message_path] = file_path
    _message_path_2_message_name_offset[message_path] = message_name_offset

    if len(md.nested_type) == 0:
        return

    message_path_prefix = message_path + "."

    for nested_md in md.nested_type:
        _process_message(nested_md, message_path_prefix, message_name_offset, file_path)


def _get_file_path(message_path: str) -> str:
    return _message_path_2_file_path[message_path]


def _get_message_name(message_path: str) -> str:
    return message_path[_message_path_2_message_name_offset[message_path]:]


def _process_file2(fd: descriptor_pb2.FileDescriptorProto) -> None:
    if len(fd.service) == 0:
        return

    for sd in fd.service:
        _process_service(sd)

    _generate_stub(fd)
    _package_name_counts.clear()
    _package_importations.clear()
    _file_path_2_package_alias.clear()


def _process_service(sd: descriptor_pb2.ServiceDescriptorProto) -> None:
    for md in sd.method:
        _process_method(md)


def _process_method(md: descriptor_pb2.MethodDescriptorProto) -> None:
    for message_path in (md.input_type, md.output_type):
        file_path = _get_file_path(message_path)

        if file_path in _file_path_2_package_alias.keys():
            continue

        package_path = _remove_postfix(file_path, ".proto").replace("/", ".") + "_pb2"

        try:
            i = package_path.rindex(".")
        except ValueError:
            package_parent_path = None
            package_name = package_path
        else:
            package_parent_path = package_path[:i]
            package_name = package_path[i + 1:]

        package_name_count = _package_name_counts.get(package_name, 0)
        _package_name_counts[package_name] = package_name_count + 1
        package_alias = package_name + "_" + str(package_name_count)
        _package_importations.append((package_parent_path, package_name, package_alias))
        _file_path_2_package_alias[file_path] = package_alias


def _get_import_statements() -> str:
    import_statements = ""

    for package_parent_path, package_name, package_alias in _package_importations:
        if package_parent_path is not None:
            import_statements += f"from {package_parent_path} "

        import_statements += f"import {package_name} as {package_alias}\n"

    return import_statements


def _get_class_path(message_path: str) -> str:
    file_path = _get_file_path(message_path)
    package_alias = _file_path_2_package_alias[file_path]
    message_name = _get_message_name(message_path)
    class_path = package_alias + "." + message_name
    return class_path


def _generate_stub(fd: descriptor_pb2.FileDescriptorProto) -> None:
    file_path = fd.name

    file_content = f"""\
# generated by protoc-gen-pbrpc. DO NOT EDIT!
# source: {file_path}
import typing
from google.protobuf import message
import async_pbrpc
"""
    file_content += _get_import_statements()
    file_content += "_MessageClass = typing.Union[typing.Type[message.Message], typing.Type[None]]\n"

    for sd in fd.service:
        service_name = sd.name
        SERVICE_NAME = _remove_postfix(service_name.replace("_", "").upper(), "SERVICE")

        request_classes_var_name = f"_{SERVICE_NAME}_REQUEST_CLASSES"
        request_class_paths = []
        file_content += f"{request_classes_var_name}: typing.Tuple[_MessageClass, ...] = (\n"

        for md in sd.method:
            if md.input_type == _VOID_PATH:
                request_class_path = "type(None)"
            else:
                request_class_path = _get_class_path(md.input_type)

            request_class_paths.append(request_class_path)
            file_content += f"    {request_class_path},\n"

        file_content += ")\n"
        response_classes_var_name = f"_{SERVICE_NAME}_RESPONSE_CLASSES"
        response_class_paths = []
        file_content += f"{response_classes_var_name}: typing.Tuple[_MessageClass, ...] = (\n"

        for md in sd.method:
            if md.output_type in (_NO_RETURN_PATH, _VOID_PATH):
                response_class_path = "type(None)"
            else:
                response_class_path = _get_class_path(md.output_type)

            response_class_paths.append(response_class_path)
            file_content += f"    {response_class_path},\n"

        file_content += ")\n"

        file_content += f"""\
class {service_name}Handler(async_pbrpc.ServiceHandler):
    SERVICE_NAME: typing.ClassVar[bytes] = b"{SERVICE_NAME}"
    METHOD_NAMES: typing.ClassVar[typing.Tuple[str, ...]] = (
"""

        for md in sd.method:
            method_name = md.name
            file_content += f"        \"{method_name}\",\n"

        file_content += f"""\
    )
    REQUEST_CLASSES: typing.ClassVar[typing.Tuple[_MessageClass, ...]] = {request_classes_var_name}
    RESPONSE_CLASSES: typing.ClassVar[typing.Tuple[_MessageClass, ...]] = {response_classes_var_name}
"""

        for method_index, md in enumerate(sd.method):
            method_name = md.name

            if md.input_type == _VOID_PATH:
                part1 = ""
            else:
                request_class_path = request_class_paths[method_index]
                part1 = f", request: {request_class_path}"

            if md.output_type in (_NO_RETURN_PATH, _VOID_PATH):
                part2 = "None"
            else:
                response_class_path = response_class_paths[method_index]
                part2 = f"{response_class_path}"

            file_content += f"""\
    @staticmethod
    def {method_name}(channel{part1}) -> {part2}:
        raise async_pbrpc.NotImplementedError()
"""

        file_content += f"""\
class {service_name}Client(async_pbrpc.ServiceClient):
    SERVICE_NAME: typing.ClassVar[bytes] = b"{SERVICE_NAME}"
    REQUEST_CLASSES: typing.ClassVar[typing.Tuple[_MessageClass, ...]] = {request_classes_var_name}
    RESPONSE_CLASSES: typing.ClassVar[typing.Tuple[_MessageClass, ...]] = {response_classes_var_name}
"""

        for method_index, md in enumerate(sd.method):
            method_name = md.name

            if md.input_type == _VOID_PATH:
                part1 = ""
            else:
                request_class_path = request_class_paths[method_index]
                part1 = f", request: {request_class_path}"

            if md.output_type == _NO_RETURN_PATH:
                part2 = "bool"
            else:
                if md.output_type == _VOID_PATH:
                    part21 = "None"
                else:
                    response_class_path = response_class_paths[method_index]
                    part21 = f"{response_class_path}"

                part2 = f"typing.Coroutine[typing.Any, typing.Any, {part21}]"

            if md.input_type == _VOID_PATH:
                part31 = "None"
            else:
                part31 = "request"

            if md.output_type == _NO_RETURN_PATH:
                part3 = f"self.call_method_without_return({method_index}, {part31}, auto_retry)"
            else:
                part3 = f"self.call_method({method_index}, {part31}, auto_retry)  # type: ignore"

            file_content += f"""\
    def {method_name}(self{part1}, *, auto_retry=False) -> {part2}:
        return {part3}
"""

    file_ = _response.file.add()
    file_.name = _remove_postfix(file_path, ".proto").replace("/", ".").replace(".", "/") \
                 + "_pbrpc.py"
    file_.content = file_content


def _remove_postfix(string: str, postfix: str) -> str:
    assert len(postfix) >= 1

    if string.endswith(postfix):
        string = string[:-len(postfix)]

    return string


_VOID_PATH = ".async_pbrpc.Void"
_NO_RETURN_PATH = ".async_pbrpc.NoReturn"
