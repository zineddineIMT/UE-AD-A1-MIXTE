# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: booking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbooking.proto\x12\x07\x62ooking\"\x19\n\x06UserId\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"=\n\x0b\x42ookingItem\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x1d\n\x06movies\x18\x02 \x03(\x0b\x32\r.booking.Date\"\'\n\x04\x44\x61te\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x11\n\tmovie_ids\x18\x02 \x03(\t\"\x07\n\x05\x45mpty2\x85\x01\n\x07\x42ooking\x12:\n\x0eGetAllBookings\x12\x0e.booking.Empty\x1a\x14.booking.BookingItem\"\x00\x30\x01\x12>\n\x11GetBookingsByUser\x12\x0f.booking.UserId\x1a\x14.booking.BookingItem\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'booking_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_USERID']._serialized_start=26
  _globals['_USERID']._serialized_end=51
  _globals['_BOOKINGITEM']._serialized_start=53
  _globals['_BOOKINGITEM']._serialized_end=114
  _globals['_DATE']._serialized_start=116
  _globals['_DATE']._serialized_end=155
  _globals['_EMPTY']._serialized_start=157
  _globals['_EMPTY']._serialized_end=164
  _globals['_BOOKING']._serialized_start=167
  _globals['_BOOKING']._serialized_end=300
# @@protoc_insertion_point(module_scope)