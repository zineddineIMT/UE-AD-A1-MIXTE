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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbooking.proto\x12\x07\x62ooking\"\x18\n\x06UserId\x12\x0e\n\x06userid\x18\x01 \x01(\t\";\n\x0b\x42ookingItem\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x1c\n\x05\x64\x61tes\x18\x02 \x03(\x0b\x32\r.booking.Date\"$\n\x04\x44\x61te\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t\"E\n\x14\x43reateBookingRequest\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x0f\n\x07movieid\x18\x03 \x01(\t\"M\n\x15\x43reateBookingResponse\x12%\n\x07\x62ooking\x18\x01 \x01(\x0b\x32\x14.booking.BookingItem\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"\x0e\n\x0c\x45mptyBooking2\xdc\x01\n\x07\x42ooking\x12\x41\n\x0eGetAllBookings\x12\x15.booking.EmptyBooking\x1a\x14.booking.BookingItem\"\x00\x30\x01\x12>\n\x11GetBookingsByUser\x12\x0f.booking.UserId\x1a\x14.booking.BookingItem\"\x00\x30\x01\x12N\n\rCreateBooking\x12\x1d.booking.CreateBookingRequest\x1a\x1e.booking.CreateBookingResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'booking_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_USERID']._serialized_start=26
  _globals['_USERID']._serialized_end=50
  _globals['_BOOKINGITEM']._serialized_start=52
  _globals['_BOOKINGITEM']._serialized_end=111
  _globals['_DATE']._serialized_start=113
  _globals['_DATE']._serialized_end=149
  _globals['_CREATEBOOKINGREQUEST']._serialized_start=151
  _globals['_CREATEBOOKINGREQUEST']._serialized_end=220
  _globals['_CREATEBOOKINGRESPONSE']._serialized_start=222
  _globals['_CREATEBOOKINGRESPONSE']._serialized_end=299
  _globals['_EMPTYBOOKING']._serialized_start=301
  _globals['_EMPTYBOOKING']._serialized_end=315
  _globals['_BOOKING']._serialized_start=318
  _globals['_BOOKING']._serialized_end=538
# @@protoc_insertion_point(module_scope)
