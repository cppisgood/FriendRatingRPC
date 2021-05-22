# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: submit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='submit.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0csubmit.proto\"\xc7\x01\n\nSubmitData\x12\x0e\n\x06handle\x18\x01 \x01(\t\x12\x13\n\x0bprofile_url\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65pt_count\x18\x03 \x01(\x05\x12\x14\n\x0csubmit_count\x18\x04 \x01(\x05\x12\x33\n\x0c\x64istribution\x18\x05 \x03(\x0b\x32\x1d.SubmitData.DistributionEntry\x1a\x33\n\x11\x44istributionEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"5\n\x11SubmitDataRequest\x12\x10\n\x08platform\x18\x01 \x01(\t\x12\x0e\n\x06handle\x18\x02 \x01(\t2E\n\x11SubmitDataService\x12\x30\n\rGetSubmitData\x12\x12.SubmitDataRequest\x1a\x0b.SubmitDatab\x06proto3'
)




_SUBMITDATA_DISTRIBUTIONENTRY = _descriptor.Descriptor(
  name='DistributionEntry',
  full_name='SubmitData.DistributionEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='SubmitData.DistributionEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='SubmitData.DistributionEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=216,
)

_SUBMITDATA = _descriptor.Descriptor(
  name='SubmitData',
  full_name='SubmitData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='handle', full_name='SubmitData.handle', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='profile_url', full_name='SubmitData.profile_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accept_count', full_name='SubmitData.accept_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='submit_count', full_name='SubmitData.submit_count', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='distribution', full_name='SubmitData.distribution', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SUBMITDATA_DISTRIBUTIONENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=216,
)


_SUBMITDATAREQUEST = _descriptor.Descriptor(
  name='SubmitDataRequest',
  full_name='SubmitDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='platform', full_name='SubmitDataRequest.platform', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='handle', full_name='SubmitDataRequest.handle', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=218,
  serialized_end=271,
)

_SUBMITDATA_DISTRIBUTIONENTRY.containing_type = _SUBMITDATA
_SUBMITDATA.fields_by_name['distribution'].message_type = _SUBMITDATA_DISTRIBUTIONENTRY
DESCRIPTOR.message_types_by_name['SubmitData'] = _SUBMITDATA
DESCRIPTOR.message_types_by_name['SubmitDataRequest'] = _SUBMITDATAREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubmitData = _reflection.GeneratedProtocolMessageType('SubmitData', (_message.Message,), {

  'DistributionEntry' : _reflection.GeneratedProtocolMessageType('DistributionEntry', (_message.Message,), {
    'DESCRIPTOR' : _SUBMITDATA_DISTRIBUTIONENTRY,
    '__module__' : 'submit_pb2'
    # @@protoc_insertion_point(class_scope:SubmitData.DistributionEntry)
    })
  ,
  'DESCRIPTOR' : _SUBMITDATA,
  '__module__' : 'submit_pb2'
  # @@protoc_insertion_point(class_scope:SubmitData)
  })
_sym_db.RegisterMessage(SubmitData)
_sym_db.RegisterMessage(SubmitData.DistributionEntry)

SubmitDataRequest = _reflection.GeneratedProtocolMessageType('SubmitDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITDATAREQUEST,
  '__module__' : 'submit_pb2'
  # @@protoc_insertion_point(class_scope:SubmitDataRequest)
  })
_sym_db.RegisterMessage(SubmitDataRequest)


_SUBMITDATA_DISTRIBUTIONENTRY._options = None

_SUBMITDATASERVICE = _descriptor.ServiceDescriptor(
  name='SubmitDataService',
  full_name='SubmitDataService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=273,
  serialized_end=342,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSubmitData',
    full_name='SubmitDataService.GetSubmitData',
    index=0,
    containing_service=None,
    input_type=_SUBMITDATAREQUEST,
    output_type=_SUBMITDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SUBMITDATASERVICE)

DESCRIPTOR.services_by_name['SubmitDataService'] = _SUBMITDATASERVICE

# @@protoc_insertion_point(module_scope)