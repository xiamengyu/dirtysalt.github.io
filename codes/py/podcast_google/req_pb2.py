# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: req.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='req.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\treq.proto\"\x82\x03\n\rSearchRequest\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.SearchRequest.Header\x12\'\n\x07payload\x18\x02 \x01(\x0b\x32\x16.SearchRequest.Payload\x1a\xe9\x01\n\x06Header\x12\"\n\x01\x61\x18\x02 \x01(\x0b\x32\x17.SearchRequest.Header.A\x12\"\n\x01\x62\x18\x04 \x01(\x0b\x32\x17.SearchRequest.Header.B\x1aP\n\x01\x41\x12$\n\x01\x62\x18\x01 \x01(\x0b\x32\x19.SearchRequest.Header.A.B\x1a%\n\x01\x42\x12\x0c\n\x01\x61\x18\x01 \x01(\x05:\x01\x36\x12\x12\n\x01\x62\x18\x02 \x01(\t:\x07\x32\x35\x38\x39\x30\x30\x35\x1a\x45\n\x01\x42\x12$\n\x01\x63\x18\x01 \x01(\x0b\x32\x19.SearchRequest.Header.B.C\x1a\x1a\n\x01\x43\x12\x15\n\x01\x61\x18\x0c \x01(\x0c:\n0x53552d6e\x1a\x35\n\x07Payload\x12\r\n\x05query\x18\x01 \x02(\t\x12\r\n\x01\x61\x18\x02 \x01(\x05:\x02\x33\x36\x12\x0c\n\x01\x62\x18\x03 \x01(\x05:\x01\x33\"\xc6\x02\n\x0eSearchResponse\x12\x0e\n\x06header\x18\x01 \x01(\t\x12(\n\x07payload\x18\x02 \x01(\x0b\x32\x17.SearchResponse.Payload\x1a\xf9\x01\n\x07Payload\x12\x30\n\x07wrapper\x18\x01 \x03(\x0b\x32\x1f.SearchResponse.Payload.Wrapper\x1ah\n\x07\x43hannel\x12\x32\n\x04meta\x18\x01 \x01(\x0b\x32$.SearchResponse.Payload.Channel.Meta\x12\x10\n\x08\x65pisodes\x18\x02 \x01(\t\x1a\x17\n\x04Meta\x12\x0f\n\x07rss_url\x18\x07 \x01(\t\x1aR\n\x07Wrapper\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\t\n\x01\x62\x18\x03 \x01(\x0c\x12\x31\n\x08\x63hannels\x18\x02 \x03(\x0b\x32\x1f.SearchResponse.Payload.Channel')
)




_SEARCHREQUEST_HEADER_A_B = _descriptor.Descriptor(
  name='B',
  full_name='SearchRequest.Header.A.B',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='SearchRequest.Header.A.B.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=6,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='SearchRequest.Header.A.B.b', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("2589005").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=274,
)

_SEARCHREQUEST_HEADER_A = _descriptor.Descriptor(
  name='A',
  full_name='SearchRequest.Header.A',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='b', full_name='SearchRequest.Header.A.b', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHREQUEST_HEADER_A_B, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=274,
)

_SEARCHREQUEST_HEADER_B_C = _descriptor.Descriptor(
  name='C',
  full_name='SearchRequest.Header.B.C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='SearchRequest.Header.B.C.a', index=0,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("0x53552d6e"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=345,
)

_SEARCHREQUEST_HEADER_B = _descriptor.Descriptor(
  name='B',
  full_name='SearchRequest.Header.B',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c', full_name='SearchRequest.Header.B.c', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHREQUEST_HEADER_B_C, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=345,
)

_SEARCHREQUEST_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='SearchRequest.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='SearchRequest.Header.a', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='SearchRequest.Header.b', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHREQUEST_HEADER_A, _SEARCHREQUEST_HEADER_B, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=345,
)

_SEARCHREQUEST_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='SearchRequest.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='SearchRequest.Payload.query', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='a', full_name='SearchRequest.Payload.a', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=36,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='SearchRequest.Payload.b', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=347,
  serialized_end=400,
)

_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='SearchRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='SearchRequest.payload', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHREQUEST_HEADER, _SEARCHREQUEST_PAYLOAD, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=400,
)


_SEARCHRESPONSE_PAYLOAD_CHANNEL_META = _descriptor.Descriptor(
  name='Meta',
  full_name='SearchResponse.Payload.Channel.Meta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rss_url', full_name='SearchResponse.Payload.Channel.Meta.rss_url', index=0,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=622,
  serialized_end=645,
)

_SEARCHRESPONSE_PAYLOAD_CHANNEL = _descriptor.Descriptor(
  name='Channel',
  full_name='SearchResponse.Payload.Channel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='SearchResponse.Payload.Channel.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='episodes', full_name='SearchResponse.Payload.Channel.episodes', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHRESPONSE_PAYLOAD_CHANNEL_META, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=541,
  serialized_end=645,
)

_SEARCHRESPONSE_PAYLOAD_WRAPPER = _descriptor.Descriptor(
  name='Wrapper',
  full_name='SearchResponse.Payload.Wrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='SearchResponse.Payload.Wrapper.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='SearchResponse.Payload.Wrapper.b', index=1,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channels', full_name='SearchResponse.Payload.Wrapper.channels', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=647,
  serialized_end=729,
)

_SEARCHRESPONSE_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='SearchResponse.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wrapper', full_name='SearchResponse.Payload.wrapper', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHRESPONSE_PAYLOAD_CHANNEL, _SEARCHRESPONSE_PAYLOAD_WRAPPER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=480,
  serialized_end=729,
)

_SEARCHRESPONSE = _descriptor.Descriptor(
  name='SearchResponse',
  full_name='SearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='SearchResponse.header', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='SearchResponse.payload', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHRESPONSE_PAYLOAD, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=729,
)

_SEARCHREQUEST_HEADER_A_B.containing_type = _SEARCHREQUEST_HEADER_A
_SEARCHREQUEST_HEADER_A.fields_by_name['b'].message_type = _SEARCHREQUEST_HEADER_A_B
_SEARCHREQUEST_HEADER_A.containing_type = _SEARCHREQUEST_HEADER
_SEARCHREQUEST_HEADER_B_C.containing_type = _SEARCHREQUEST_HEADER_B
_SEARCHREQUEST_HEADER_B.fields_by_name['c'].message_type = _SEARCHREQUEST_HEADER_B_C
_SEARCHREQUEST_HEADER_B.containing_type = _SEARCHREQUEST_HEADER
_SEARCHREQUEST_HEADER.fields_by_name['a'].message_type = _SEARCHREQUEST_HEADER_A
_SEARCHREQUEST_HEADER.fields_by_name['b'].message_type = _SEARCHREQUEST_HEADER_B
_SEARCHREQUEST_HEADER.containing_type = _SEARCHREQUEST
_SEARCHREQUEST_PAYLOAD.containing_type = _SEARCHREQUEST
_SEARCHREQUEST.fields_by_name['header'].message_type = _SEARCHREQUEST_HEADER
_SEARCHREQUEST.fields_by_name['payload'].message_type = _SEARCHREQUEST_PAYLOAD
_SEARCHRESPONSE_PAYLOAD_CHANNEL_META.containing_type = _SEARCHRESPONSE_PAYLOAD_CHANNEL
_SEARCHRESPONSE_PAYLOAD_CHANNEL.fields_by_name['meta'].message_type = _SEARCHRESPONSE_PAYLOAD_CHANNEL_META
_SEARCHRESPONSE_PAYLOAD_CHANNEL.containing_type = _SEARCHRESPONSE_PAYLOAD
_SEARCHRESPONSE_PAYLOAD_WRAPPER.fields_by_name['channels'].message_type = _SEARCHRESPONSE_PAYLOAD_CHANNEL
_SEARCHRESPONSE_PAYLOAD_WRAPPER.containing_type = _SEARCHRESPONSE_PAYLOAD
_SEARCHRESPONSE_PAYLOAD.fields_by_name['wrapper'].message_type = _SEARCHRESPONSE_PAYLOAD_WRAPPER
_SEARCHRESPONSE_PAYLOAD.containing_type = _SEARCHRESPONSE
_SEARCHRESPONSE.fields_by_name['payload'].message_type = _SEARCHRESPONSE_PAYLOAD
DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['SearchResponse'] = _SEARCHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), dict(

  Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(

    A = _reflection.GeneratedProtocolMessageType('A', (_message.Message,), dict(

      B = _reflection.GeneratedProtocolMessageType('B', (_message.Message,), dict(
        DESCRIPTOR = _SEARCHREQUEST_HEADER_A_B,
        __module__ = 'req_pb2'
        # @@protoc_insertion_point(class_scope:SearchRequest.Header.A.B)
        ))
      ,
      DESCRIPTOR = _SEARCHREQUEST_HEADER_A,
      __module__ = 'req_pb2'
      # @@protoc_insertion_point(class_scope:SearchRequest.Header.A)
      ))
    ,

    B = _reflection.GeneratedProtocolMessageType('B', (_message.Message,), dict(

      C = _reflection.GeneratedProtocolMessageType('C', (_message.Message,), dict(
        DESCRIPTOR = _SEARCHREQUEST_HEADER_B_C,
        __module__ = 'req_pb2'
        # @@protoc_insertion_point(class_scope:SearchRequest.Header.B.C)
        ))
      ,
      DESCRIPTOR = _SEARCHREQUEST_HEADER_B,
      __module__ = 'req_pb2'
      # @@protoc_insertion_point(class_scope:SearchRequest.Header.B)
      ))
    ,
    DESCRIPTOR = _SEARCHREQUEST_HEADER,
    __module__ = 'req_pb2'
    # @@protoc_insertion_point(class_scope:SearchRequest.Header)
    ))
  ,

  Payload = _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), dict(
    DESCRIPTOR = _SEARCHREQUEST_PAYLOAD,
    __module__ = 'req_pb2'
    # @@protoc_insertion_point(class_scope:SearchRequest.Payload)
    ))
  ,
  DESCRIPTOR = _SEARCHREQUEST,
  __module__ = 'req_pb2'
  # @@protoc_insertion_point(class_scope:SearchRequest)
  ))
_sym_db.RegisterMessage(SearchRequest)
_sym_db.RegisterMessage(SearchRequest.Header)
_sym_db.RegisterMessage(SearchRequest.Header.A)
_sym_db.RegisterMessage(SearchRequest.Header.A.B)
_sym_db.RegisterMessage(SearchRequest.Header.B)
_sym_db.RegisterMessage(SearchRequest.Header.B.C)
_sym_db.RegisterMessage(SearchRequest.Payload)

SearchResponse = _reflection.GeneratedProtocolMessageType('SearchResponse', (_message.Message,), dict(

  Payload = _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), dict(

    Channel = _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), dict(

      Meta = _reflection.GeneratedProtocolMessageType('Meta', (_message.Message,), dict(
        DESCRIPTOR = _SEARCHRESPONSE_PAYLOAD_CHANNEL_META,
        __module__ = 'req_pb2'
        # @@protoc_insertion_point(class_scope:SearchResponse.Payload.Channel.Meta)
        ))
      ,
      DESCRIPTOR = _SEARCHRESPONSE_PAYLOAD_CHANNEL,
      __module__ = 'req_pb2'
      # @@protoc_insertion_point(class_scope:SearchResponse.Payload.Channel)
      ))
    ,

    Wrapper = _reflection.GeneratedProtocolMessageType('Wrapper', (_message.Message,), dict(
      DESCRIPTOR = _SEARCHRESPONSE_PAYLOAD_WRAPPER,
      __module__ = 'req_pb2'
      # @@protoc_insertion_point(class_scope:SearchResponse.Payload.Wrapper)
      ))
    ,
    DESCRIPTOR = _SEARCHRESPONSE_PAYLOAD,
    __module__ = 'req_pb2'
    # @@protoc_insertion_point(class_scope:SearchResponse.Payload)
    ))
  ,
  DESCRIPTOR = _SEARCHRESPONSE,
  __module__ = 'req_pb2'
  # @@protoc_insertion_point(class_scope:SearchResponse)
  ))
_sym_db.RegisterMessage(SearchResponse)
_sym_db.RegisterMessage(SearchResponse.Payload)
_sym_db.RegisterMessage(SearchResponse.Payload.Channel)
_sym_db.RegisterMessage(SearchResponse.Payload.Channel.Meta)
_sym_db.RegisterMessage(SearchResponse.Payload.Wrapper)


# @@protoc_insertion_point(module_scope)
