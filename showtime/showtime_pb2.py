# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: showtime.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eshowtime.proto\"(\n\x08Schedule\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t\"\x14\n\x04\x44\x61te\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\"\x0f\n\rEmptySchedule2c\n\x08Showtime\x12\x30\n\x0fGetAllShowtimes\x12\x0e.EmptySchedule\x1a\t.Schedule\"\x00\x30\x01\x12%\n\x0fGetMoviesByDate\x12\x05.Date\x1a\t.Schedule\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'showtime_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_SCHEDULE']._serialized_start=18
  _globals['_SCHEDULE']._serialized_end=58
  _globals['_DATE']._serialized_start=60
  _globals['_DATE']._serialized_end=80
  _globals['_EMPTYSCHEDULE']._serialized_start=82
  _globals['_EMPTYSCHEDULE']._serialized_end=97
  _globals['_SHOWTIME']._serialized_start=99
  _globals['_SHOWTIME']._serialized_end=198
# @@protoc_insertion_point(module_scope)