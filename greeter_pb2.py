# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greeter.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greeter.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\rgreeter.proto\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t21\n\x07Greeter\x12&\n\x08SayHello\x12\r.HelloRequest\x1a\x0b.HelloReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'greeter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_HELLOREQUEST']._serialized_start = 17
    _globals['_HELLOREQUEST']._serialized_end = 45
    _globals['_HELLOREPLY']._serialized_start = 47
    _globals['_HELLOREPLY']._serialized_end = 76
    _globals['_GREETER']._serialized_start = 78
    _globals['_GREETER']._serialized_end = 127
# @@protoc_insertion_point(module_scope)
