# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='noteworthy_reservation',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0emessages.proto\x12\x16noteworthy_reservation\"7\n\x12ReservationRequest\x12\x0e\n\x06\x64omain\x18\x01 \x01(\t\x12\x11\n\tauth_code\x18\x02 \x01(\t\"5\n\x13ReservationResponse\x12\x0f\n\x07success\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"A\n\x0bLinkRequest\x12\x0e\n\x06\x64omain\x18\x01 \x01(\t\x12\x0f\n\x07pub_key\x18\x02 \x01(\t\x12\x11\n\tauth_code\x18\x03 \x01(\t\"\x93\x01\n\x0cLinkResponse\x12\x18\n\x10link_wg_endpoint\x18\x01 \x01(\t\x12\x16\n\x0elink_wg_pubkey\x18\x02 \x01(\t\x12\x1f\n\x17link_udp_proxy_endpoint\x18\x03 \x01(\t\x12!\n\x19link_udp_proxy_endpoint_2\x18\x04 \x01(\t\x12\r\n\x05\x65rror\x18\x05 \x01(\tb\x06proto3'
)




_RESERVATIONREQUEST = _descriptor.Descriptor(
  name='ReservationRequest',
  full_name='noteworthy_reservation.ReservationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain', full_name='noteworthy_reservation.ReservationRequest.domain', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth_code', full_name='noteworthy_reservation.ReservationRequest.auth_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=97,
)


_RESERVATIONRESPONSE = _descriptor.Descriptor(
  name='ReservationResponse',
  full_name='noteworthy_reservation.ReservationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='noteworthy_reservation.ReservationResponse.success', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='noteworthy_reservation.ReservationResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=152,
)


_LINKREQUEST = _descriptor.Descriptor(
  name='LinkRequest',
  full_name='noteworthy_reservation.LinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain', full_name='noteworthy_reservation.LinkRequest.domain', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pub_key', full_name='noteworthy_reservation.LinkRequest.pub_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth_code', full_name='noteworthy_reservation.LinkRequest.auth_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=219,
)


_LINKRESPONSE = _descriptor.Descriptor(
  name='LinkResponse',
  full_name='noteworthy_reservation.LinkResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='link_wg_endpoint', full_name='noteworthy_reservation.LinkResponse.link_wg_endpoint', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link_wg_pubkey', full_name='noteworthy_reservation.LinkResponse.link_wg_pubkey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link_udp_proxy_endpoint', full_name='noteworthy_reservation.LinkResponse.link_udp_proxy_endpoint', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link_udp_proxy_endpoint_2', full_name='noteworthy_reservation.LinkResponse.link_udp_proxy_endpoint_2', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='noteworthy_reservation.LinkResponse.error', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=369,
)

DESCRIPTOR.message_types_by_name['ReservationRequest'] = _RESERVATIONREQUEST
DESCRIPTOR.message_types_by_name['ReservationResponse'] = _RESERVATIONRESPONSE
DESCRIPTOR.message_types_by_name['LinkRequest'] = _LINKREQUEST
DESCRIPTOR.message_types_by_name['LinkResponse'] = _LINKRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReservationRequest = _reflection.GeneratedProtocolMessageType('ReservationRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESERVATIONREQUEST,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:noteworthy_reservation.ReservationRequest)
  })
_sym_db.RegisterMessage(ReservationRequest)

ReservationResponse = _reflection.GeneratedProtocolMessageType('ReservationResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESERVATIONRESPONSE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:noteworthy_reservation.ReservationResponse)
  })
_sym_db.RegisterMessage(ReservationResponse)

LinkRequest = _reflection.GeneratedProtocolMessageType('LinkRequest', (_message.Message,), {
  'DESCRIPTOR' : _LINKREQUEST,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:noteworthy_reservation.LinkRequest)
  })
_sym_db.RegisterMessage(LinkRequest)

LinkResponse = _reflection.GeneratedProtocolMessageType('LinkResponse', (_message.Message,), {
  'DESCRIPTOR' : _LINKRESPONSE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:noteworthy_reservation.LinkResponse)
  })
_sym_db.RegisterMessage(LinkResponse)


# @@protoc_insertion_point(module_scope)
