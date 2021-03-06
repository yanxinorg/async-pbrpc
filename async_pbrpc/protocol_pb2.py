# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pbrpc/protocol.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pbrpc/protocol.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x14pbrpc/protocol.proto\"d\n\tHandshake\x12\x0f\n\x07timeout\x18\x01 \x01(\r\x12\x1c\n\x14outgoing_window_size\x18\x02 \x01(\r\x12\x1c\n\x14incoming_window_size\x18\x03 \x01(\r\x12\n\n\x02id\x18\x04 \x01(\x0c\"T\n\rRequestHeader\x12\x17\n\x0fsequence_number\x18\x01 \x01(\r\x12\x14\n\x0cservice_name\x18\x02 \x01(\x0c\x12\x14\n\x0cmethod_index\x18\x03 \x01(\r\":\n\x07Request\x12\x1e\n\x06header\x18\x01 \x01(\x0b\x32\x0e.RequestHeader\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\"=\n\x0eResponseHeader\x12\x17\n\x0fsequence_number\x18\x01 \x01(\r\x12\x12\n\nerror_code\x18\x02 \x01(\r\"<\n\x08Response\x12\x1f\n\x06header\x18\x01 \x01(\x0b\x32\x0f.ResponseHeader\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\"\x0b\n\tHeartbeat*b\n\x07Message\x12\x15\n\x11MESSAGE_HANDSHAKE\x10\x00\x12\x13\n\x0fMESSAGE_REQUEST\x10\x01\x12\x14\n\x10MESSAGE_RESPONSE\x10\x02\x12\x15\n\x11MESSAGE_HEARTBEAT\x10\x03*\x93\x01\n\x05\x45rror\x12\x0c\n\x08\x45RROR_NO\x10\x00\x12\x16\n\x12\x45RROR_CHANNEL_BUSY\x10\x01\x12\x19\n\x15\x45RROR_NOT_IMPLEMENTED\x10\x02\x12\x15\n\x11\x45RROR_BAD_REQUEST\x10\x03\x12\x19\n\x15\x45RROR_INTERNAL_SERVER\x10\x04\x12\x17\n\x12\x45RROR_USER_DEFINED\x10\x80\x02\x62\x06proto3')
)

_MESSAGE = _descriptor.EnumDescriptor(
  name='Message',
  full_name='Message',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MESSAGE_HANDSHAKE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE_REQUEST', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE_RESPONSE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE_HEARTBEAT', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=410,
  serialized_end=508,
)
_sym_db.RegisterEnumDescriptor(_MESSAGE)

Message = enum_type_wrapper.EnumTypeWrapper(_MESSAGE)
_ERROR = _descriptor.EnumDescriptor(
  name='Error',
  full_name='Error',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ERROR_NO', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_CHANNEL_BUSY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_IMPLEMENTED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_BAD_REQUEST', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INTERNAL_SERVER', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_USER_DEFINED', index=5, number=256,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=511,
  serialized_end=658,
)
_sym_db.RegisterEnumDescriptor(_ERROR)

Error = enum_type_wrapper.EnumTypeWrapper(_ERROR)
MESSAGE_HANDSHAKE = 0
MESSAGE_REQUEST = 1
MESSAGE_RESPONSE = 2
MESSAGE_HEARTBEAT = 3
ERROR_NO = 0
ERROR_CHANNEL_BUSY = 1
ERROR_NOT_IMPLEMENTED = 2
ERROR_BAD_REQUEST = 3
ERROR_INTERNAL_SERVER = 4
ERROR_USER_DEFINED = 256



_HANDSHAKE = _descriptor.Descriptor(
  name='Handshake',
  full_name='Handshake',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeout', full_name='Handshake.timeout', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outgoing_window_size', full_name='Handshake.outgoing_window_size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='incoming_window_size', full_name='Handshake.incoming_window_size', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Handshake.id', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=124,
)


_REQUESTHEADER = _descriptor.Descriptor(
  name='RequestHeader',
  full_name='RequestHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='RequestHeader.sequence_number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='service_name', full_name='RequestHeader.service_name', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method_index', full_name='RequestHeader.method_index', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=210,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Request.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='Request.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=270,
)


_RESPONSEHEADER = _descriptor.Descriptor(
  name='ResponseHeader',
  full_name='ResponseHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='ResponseHeader.sequence_number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='ResponseHeader.error_code', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=333,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Response.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='Response.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=335,
  serialized_end=395,
)


_HEARTBEAT = _descriptor.Descriptor(
  name='Heartbeat',
  full_name='Heartbeat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=397,
  serialized_end=408,
)

_REQUEST.fields_by_name['header'].message_type = _REQUESTHEADER
_RESPONSE.fields_by_name['header'].message_type = _RESPONSEHEADER
DESCRIPTOR.message_types_by_name['Handshake'] = _HANDSHAKE
DESCRIPTOR.message_types_by_name['RequestHeader'] = _REQUESTHEADER
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['ResponseHeader'] = _RESPONSEHEADER
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Heartbeat'] = _HEARTBEAT
DESCRIPTOR.enum_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.enum_types_by_name['Error'] = _ERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Handshake = _reflection.GeneratedProtocolMessageType('Handshake', (_message.Message,), dict(
  DESCRIPTOR = _HANDSHAKE,
  __module__ = 'pbrpc.protocol_pb2'
  # @@protoc_insertion_point(class_scope:Handshake)
  ))
_sym_db.RegisterMessage(Handshake)

RequestHeader = _reflection.GeneratedProtocolMessageType('RequestHeader', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTHEADER,
  __module__ = 'pbrpc.protocol_pb2'
  # @@protoc_insertion_point(class_scope:RequestHeader)
  ))
_sym_db.RegisterMessage(RequestHeader)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'pbrpc.protocol_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  ))
_sym_db.RegisterMessage(Request)

ResponseHeader = _reflection.GeneratedProtocolMessageType('ResponseHeader', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEHEADER,
  __module__ = 'pbrpc.protocol_pb2'
  # @@protoc_insertion_point(class_scope:ResponseHeader)
  ))
_sym_db.RegisterMessage(ResponseHeader)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'pbrpc.protocol_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  ))
_sym_db.RegisterMessage(Response)

Heartbeat = _reflection.GeneratedProtocolMessageType('Heartbeat', (_message.Message,), dict(
  DESCRIPTOR = _HEARTBEAT,
  __module__ = 'pbrpc.protocol_pb2'
  # @@protoc_insertion_point(class_scope:Heartbeat)
  ))
_sym_db.RegisterMessage(Heartbeat)


# @@protoc_insertion_point(module_scope)
