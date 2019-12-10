# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analyzer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import plugin_pb2 as plugin__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='analyzer.proto',
  package='pulumirpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x61nalyzer.proto\x12\tpulumirpc\x1a\x0cplugin.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x9b\x01\n\x0e\x41nalyzeRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0b\n\x03urn\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x33\n\x07options\x18\x05 \x01(\x0b\x32\".pulumirpc.AnalyzerResourceOptions\"\x9d\x01\n\x10\x41nalyzerResource\x12\x0c\n\x04type\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0b\n\x03urn\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x33\n\x07options\x18\x05 \x01(\x0b\x32\".pulumirpc.AnalyzerResourceOptions\"\xa1\x02\n\x17\x41nalyzerResourceOptions\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0f\n\x07protect\x18\x02 \x01(\x08\x12\x14\n\x0c\x64\x65pendencies\x18\x03 \x03(\t\x12\x10\n\x08provider\x18\x04 \x01(\t\x12\x1f\n\x17\x61\x64\x64itionalSecretOutputs\x18\x05 \x03(\t\x12\x0f\n\x07\x61liases\x18\x06 \x03(\t\x12I\n\x0e\x63ustomTimeouts\x18\x07 \x01(\x0b\x32\x31.pulumirpc.AnalyzerResourceOptions.CustomTimeouts\x1a@\n\x0e\x43ustomTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06update\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x03 \x01(\t\"E\n\x13\x41nalyzeStackRequest\x12.\n\tresources\x18\x01 \x03(\x0b\x32\x1b.pulumirpc.AnalyzerResource\"D\n\x0f\x41nalyzeResponse\x12\x31\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x1c.pulumirpc.AnalyzeDiagnostic\"\xd2\x01\n\x11\x41nalyzeDiagnostic\x12\x12\n\npolicyName\x18\x01 \x01(\t\x12\x16\n\x0epolicyPackName\x18\x02 \x01(\t\x12\x19\n\x11policyPackVersion\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0f\n\x07message\x18\x05 \x01(\t\x12\x0c\n\x04tags\x18\x06 \x03(\t\x12\x35\n\x10\x65nforcementLevel\x18\x07 \x01(\x0e\x32\x1b.pulumirpc.EnforcementLevel\x12\x0b\n\x03urn\x18\x08 \x01(\t\"Z\n\x0c\x41nalyzerInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64isplayName\x18\x02 \x01(\t\x12\'\n\x08policies\x18\x03 \x03(\x0b\x32\x15.pulumirpc.PolicyInfo\"\x8c\x01\n\nPolicyInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64isplayName\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x35\n\x10\x65nforcementLevel\x18\x05 \x01(\x0e\x32\x1b.pulumirpc.EnforcementLevel*/\n\x10\x45nforcementLevel\x12\x0c\n\x08\x41\x44VISORY\x10\x00\x12\r\n\tMANDATORY\x10\x01\x32\xa4\x02\n\x08\x41nalyzer\x12\x42\n\x07\x41nalyze\x12\x19.pulumirpc.AnalyzeRequest\x1a\x1a.pulumirpc.AnalyzeResponse\"\x00\x12L\n\x0c\x41nalyzeStack\x12\x1e.pulumirpc.AnalyzeStackRequest\x1a\x1a.pulumirpc.AnalyzeResponse\"\x00\x12\x44\n\x0fGetAnalyzerInfo\x12\x16.google.protobuf.Empty\x1a\x17.pulumirpc.AnalyzerInfo\"\x00\x12@\n\rGetPluginInfo\x12\x16.google.protobuf.Empty\x1a\x15.pulumirpc.PluginInfo\"\x00\x62\x06proto3')
  ,
  dependencies=[plugin__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])

_ENFORCEMENTLEVEL = _descriptor.EnumDescriptor(
  name='EnforcementLevel',
  full_name='pulumirpc.EnforcementLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADVISORY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MANDATORY', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1301,
  serialized_end=1348,
)
_sym_db.RegisterEnumDescriptor(_ENFORCEMENTLEVEL)

EnforcementLevel = enum_type_wrapper.EnumTypeWrapper(_ENFORCEMENTLEVEL)
ADVISORY = 0
MANDATORY = 1



_ANALYZEREQUEST = _descriptor.Descriptor(
  name='AnalyzeRequest',
  full_name='pulumirpc.AnalyzeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pulumirpc.AnalyzeRequest.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='pulumirpc.AnalyzeRequest.properties', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urn', full_name='pulumirpc.AnalyzeRequest.urn', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='pulumirpc.AnalyzeRequest.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='pulumirpc.AnalyzeRequest.options', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=103,
  serialized_end=258,
)


_ANALYZERRESOURCE = _descriptor.Descriptor(
  name='AnalyzerResource',
  full_name='pulumirpc.AnalyzerResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pulumirpc.AnalyzerResource.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='pulumirpc.AnalyzerResource.properties', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urn', full_name='pulumirpc.AnalyzerResource.urn', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='pulumirpc.AnalyzerResource.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='pulumirpc.AnalyzerResource.options', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=261,
  serialized_end=418,
)


_ANALYZERRESOURCEOPTIONS_CUSTOMTIMEOUTS = _descriptor.Descriptor(
  name='CustomTimeouts',
  full_name='pulumirpc.AnalyzerResourceOptions.CustomTimeouts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='create', full_name='pulumirpc.AnalyzerResourceOptions.CustomTimeouts.create', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='pulumirpc.AnalyzerResourceOptions.CustomTimeouts.update', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delete', full_name='pulumirpc.AnalyzerResourceOptions.CustomTimeouts.delete', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=646,
  serialized_end=710,
)

_ANALYZERRESOURCEOPTIONS = _descriptor.Descriptor(
  name='AnalyzerResourceOptions',
  full_name='pulumirpc.AnalyzerResourceOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='pulumirpc.AnalyzerResourceOptions.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protect', full_name='pulumirpc.AnalyzerResourceOptions.protect', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dependencies', full_name='pulumirpc.AnalyzerResourceOptions.dependencies', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provider', full_name='pulumirpc.AnalyzerResourceOptions.provider', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='additionalSecretOutputs', full_name='pulumirpc.AnalyzerResourceOptions.additionalSecretOutputs', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aliases', full_name='pulumirpc.AnalyzerResourceOptions.aliases', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customTimeouts', full_name='pulumirpc.AnalyzerResourceOptions.customTimeouts', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ANALYZERRESOURCEOPTIONS_CUSTOMTIMEOUTS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=421,
  serialized_end=710,
)


_ANALYZESTACKREQUEST = _descriptor.Descriptor(
  name='AnalyzeStackRequest',
  full_name='pulumirpc.AnalyzeStackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resources', full_name='pulumirpc.AnalyzeStackRequest.resources', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=712,
  serialized_end=781,
)


_ANALYZERESPONSE = _descriptor.Descriptor(
  name='AnalyzeResponse',
  full_name='pulumirpc.AnalyzeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='diagnostics', full_name='pulumirpc.AnalyzeResponse.diagnostics', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=783,
  serialized_end=851,
)


_ANALYZEDIAGNOSTIC = _descriptor.Descriptor(
  name='AnalyzeDiagnostic',
  full_name='pulumirpc.AnalyzeDiagnostic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='policyName', full_name='pulumirpc.AnalyzeDiagnostic.policyName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='policyPackName', full_name='pulumirpc.AnalyzeDiagnostic.policyPackName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='policyPackVersion', full_name='pulumirpc.AnalyzeDiagnostic.policyPackVersion', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='pulumirpc.AnalyzeDiagnostic.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='pulumirpc.AnalyzeDiagnostic.message', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='pulumirpc.AnalyzeDiagnostic.tags', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enforcementLevel', full_name='pulumirpc.AnalyzeDiagnostic.enforcementLevel', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urn', full_name='pulumirpc.AnalyzeDiagnostic.urn', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=854,
  serialized_end=1064,
)


_ANALYZERINFO = _descriptor.Descriptor(
  name='AnalyzerInfo',
  full_name='pulumirpc.AnalyzerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pulumirpc.AnalyzerInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='displayName', full_name='pulumirpc.AnalyzerInfo.displayName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='policies', full_name='pulumirpc.AnalyzerInfo.policies', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1066,
  serialized_end=1156,
)


_POLICYINFO = _descriptor.Descriptor(
  name='PolicyInfo',
  full_name='pulumirpc.PolicyInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pulumirpc.PolicyInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='displayName', full_name='pulumirpc.PolicyInfo.displayName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='pulumirpc.PolicyInfo.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='pulumirpc.PolicyInfo.message', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enforcementLevel', full_name='pulumirpc.PolicyInfo.enforcementLevel', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1159,
  serialized_end=1299,
)

_ANALYZEREQUEST.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_ANALYZEREQUEST.fields_by_name['options'].message_type = _ANALYZERRESOURCEOPTIONS
_ANALYZERRESOURCE.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_ANALYZERRESOURCE.fields_by_name['options'].message_type = _ANALYZERRESOURCEOPTIONS
_ANALYZERRESOURCEOPTIONS_CUSTOMTIMEOUTS.containing_type = _ANALYZERRESOURCEOPTIONS
_ANALYZERRESOURCEOPTIONS.fields_by_name['customTimeouts'].message_type = _ANALYZERRESOURCEOPTIONS_CUSTOMTIMEOUTS
_ANALYZESTACKREQUEST.fields_by_name['resources'].message_type = _ANALYZERRESOURCE
_ANALYZERESPONSE.fields_by_name['diagnostics'].message_type = _ANALYZEDIAGNOSTIC
_ANALYZEDIAGNOSTIC.fields_by_name['enforcementLevel'].enum_type = _ENFORCEMENTLEVEL
_ANALYZERINFO.fields_by_name['policies'].message_type = _POLICYINFO
_POLICYINFO.fields_by_name['enforcementLevel'].enum_type = _ENFORCEMENTLEVEL
DESCRIPTOR.message_types_by_name['AnalyzeRequest'] = _ANALYZEREQUEST
DESCRIPTOR.message_types_by_name['AnalyzerResource'] = _ANALYZERRESOURCE
DESCRIPTOR.message_types_by_name['AnalyzerResourceOptions'] = _ANALYZERRESOURCEOPTIONS
DESCRIPTOR.message_types_by_name['AnalyzeStackRequest'] = _ANALYZESTACKREQUEST
DESCRIPTOR.message_types_by_name['AnalyzeResponse'] = _ANALYZERESPONSE
DESCRIPTOR.message_types_by_name['AnalyzeDiagnostic'] = _ANALYZEDIAGNOSTIC
DESCRIPTOR.message_types_by_name['AnalyzerInfo'] = _ANALYZERINFO
DESCRIPTOR.message_types_by_name['PolicyInfo'] = _POLICYINFO
DESCRIPTOR.enum_types_by_name['EnforcementLevel'] = _ENFORCEMENTLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnalyzeRequest = _reflection.GeneratedProtocolMessageType('AnalyzeRequest', (_message.Message,), dict(
  DESCRIPTOR = _ANALYZEREQUEST,
  __module__ = 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzeRequest)
  ))
_sym_db.RegisterMessage(AnalyzeRequest)

AnalyzerResource = _reflection.GeneratedProtocolMessageType('AnalyzerResource', (_message.Message,), dict(
  DESCRIPTOR = _ANALYZERRESOURCE,
  __module__ = 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzerResource)
  ))
_sym_db.RegisterMessage(AnalyzerResource)

AnalyzerResourceOptions = _reflection.GeneratedProtocolMessageType('AnalyzerResourceOptions', (_message.Message,), dict(

  CustomTimeouts = _reflection.GeneratedProtocolMessageType('CustomTimeouts', (_message.Message,), dict(
    DESCRIPTOR = _ANALYZERRESOURCEOPTIONS_CUSTOMTIMEOUTS,
    __module__ = 'analyzer_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzerResourceOptions.CustomTimeouts)
    ))
  ,
  DESCRIPTOR = _ANALYZERRESOURCEOPTIONS,
  __module__ = 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzerResourceOptions)
  ))
_sym_db.RegisterMessage(AnalyzerResourceOptions)
_sym_db.RegisterMessage(AnalyzerResourceOptions.CustomTimeouts)

AnalyzeStackRequest = _reflection.GeneratedProtocolMessageType('AnalyzeStackRequest', (_message.Message,), dict(
  DESCRIPTOR = _ANALYZESTACKREQUEST,
  __module__ = 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzeStackRequest)
  ))
_sym_db.RegisterMessage(AnalyzeStackRequest)

AnalyzeResponse = _reflection.GeneratedProtocolMessageType('AnalyzeResponse', (_message.Message,), dict(
  DESCRIPTOR = _ANALYZERESPONSE,
  __module__ = 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzeResponse)
  ))
_sym_db.RegisterMessage(AnalyzeResponse)

AnalyzeDiagnostic = _reflection.GeneratedProtocolMessageType('AnalyzeDiagnostic', (_message.Message,), dict(
  DESCRIPTOR = _ANALYZEDIAGNOSTIC,
  __module__ = 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzeDiagnostic)
  ))
_sym_db.RegisterMessage(AnalyzeDiagnostic)

AnalyzerInfo = _reflection.GeneratedProtocolMessageType('AnalyzerInfo', (_message.Message,), dict(
  DESCRIPTOR = _ANALYZERINFO,
  __module__ = 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzerInfo)
  ))
_sym_db.RegisterMessage(AnalyzerInfo)

PolicyInfo = _reflection.GeneratedProtocolMessageType('PolicyInfo', (_message.Message,), dict(
  DESCRIPTOR = _POLICYINFO,
  __module__ = 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.PolicyInfo)
  ))
_sym_db.RegisterMessage(PolicyInfo)



_ANALYZER = _descriptor.ServiceDescriptor(
  name='Analyzer',
  full_name='pulumirpc.Analyzer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1351,
  serialized_end=1643,
  methods=[
  _descriptor.MethodDescriptor(
    name='Analyze',
    full_name='pulumirpc.Analyzer.Analyze',
    index=0,
    containing_service=None,
    input_type=_ANALYZEREQUEST,
    output_type=_ANALYZERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AnalyzeStack',
    full_name='pulumirpc.Analyzer.AnalyzeStack',
    index=1,
    containing_service=None,
    input_type=_ANALYZESTACKREQUEST,
    output_type=_ANALYZERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAnalyzerInfo',
    full_name='pulumirpc.Analyzer.GetAnalyzerInfo',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_ANALYZERINFO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPluginInfo',
    full_name='pulumirpc.Analyzer.GetPluginInfo',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=plugin__pb2._PLUGININFO,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ANALYZER)

DESCRIPTOR.services_by_name['Analyzer'] = _ANALYZER

# @@protoc_insertion_point(module_scope)
