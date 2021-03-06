import asyncio
import enum
import logging
import ssl
import typing

from asyncio_toolkit import utils
from asyncio_toolkit.typing import BytesLike, Coroutine

from . import errors


class TransportPolicy(typing.NamedTuple):
    ssl_context: typing.Optional[ssl.SSLContext]=None
    read_buffer_size: int=1 << 16
    max_message_size: int=1 << 16


class Transport:
    _logger = logging.getLogger()
    _policy = TransportPolicy()

    def __init__(self, loop: typing.Optional[asyncio.AbstractEventLoop]
                 , logger: typing.Optional[logging.Logger]
                 , policy: typing.Optional[TransportPolicy]) -> None:
        if loop is None:
            self._loop = asyncio.get_event_loop()
        else:
            self._loop = loop

        if logger is not None and logger is not self._logger:
            self._logger = logger

        if policy is not None and policy is not self._policy:
            self._policy = policy

        self._is_closed = True
        self._stream_reader: asyncio.StreamReader
        self._stream_writer: asyncio.StreamWriter

    def connect(self, host_name: str, port_number: int, connect_timeout: float) -> Coroutine[None]:
        assert self._is_closed
        return utils.wait_for1(self._connect(host_name, port_number), connect_timeout
                               , loop=self._loop)

    def accept(self, stream_reader: asyncio.StreamReader
               , stream_writer: asyncio.StreamWriter) -> None:
        assert self._is_closed
        self._stream_reader, self._stream_writer = stream_reader, stream_writer
        self._is_closed = False

    def write(self, message_flags: int, message_payload: BytesLike) -> None:
        assert not self._is_closed
        message_payload_size = len(message_payload)

        if 8 + message_payload_size > self._policy.max_message_size:
            raise errors.MessageTooLargeError("message_payload_size={!r}"
                                              .format(message_payload_size))

        message_header = message_flags.to_bytes(4, "big") + message_payload_size.to_bytes(4, "big")
        self._stream_writer.write(message_header)
        self._stream_writer.write(message_payload)

    def read(self, read_timeout: float) -> Coroutine[typing.Tuple[int, bytes]]:
        assert not self._is_closed
        return utils.wait_for1(self._read(), read_timeout, loop=self._loop)

    def close(self) -> None:
        assert not self._is_closed
        self._stream_writer.close()
        self._is_closed = True

    def get_loop(self) -> asyncio.AbstractEventLoop:
        return self._loop

    def get_logger(self) -> logging.Logger:
        return self._logger

    def get_policy(self) -> TransportPolicy:
        return self._policy

    def is_closed(self) -> bool:
        return self._is_closed

    async def _connect(self, host_name: str, port_number: int) -> None:
        self._stream_reader, self._stream_writer = await asyncio.open_connection(
            host_name,
            port_number,
            loop=self._loop,
            ssl=self._policy.ssl_context,
            limit=self._policy.read_buffer_size,
        )

        self._is_closed = False

    async def _read(self) -> typing.Tuple[int, bytes]:
        message_header = await self._stream_reader.readexactly(8)
        message_flags = int.from_bytes(message_header[:4], "big")
        message_payload_size = int.from_bytes(message_header[4:], "big")

        if 8 + message_payload_size > self._policy.max_message_size:
            raise errors.MessageTooLargeError("message_payload_size={!r}"
                                              .format(message_payload_size))

        message_payload = await self._stream_reader.readexactly(message_payload_size)
        return message_flags, message_payload
