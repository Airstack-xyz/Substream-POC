# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sf/substreams/v1/modules.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esf/substreams/v1/modules.proto\x12\x10sf.substreams.v1\"s\n\x07Modules\x12\x32\n\x07modules\x18\x01 \x03(\x0b\x32\x18.sf.substreams.v1.ModuleR\x07modules\x12\x34\n\x08\x62inaries\x18\x02 \x03(\x0b\x32\x18.sf.substreams.v1.BinaryR\x08\x62inaries\"6\n\x06\x42inary\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x18\n\x07\x63ontent\x18\x02 \x01(\x0cR\x07\x63ontent\"\xc2\t\n\x06Module\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12=\n\x08kind_map\x18\x02 \x01(\x0b\x32 .sf.substreams.v1.Module.KindMapH\x00R\x07kindMap\x12\x43\n\nkind_store\x18\x03 \x01(\x0b\x32\".sf.substreams.v1.Module.KindStoreH\x00R\tkindStore\x12!\n\x0c\x62inary_index\x18\x04 \x01(\rR\x0b\x62inaryIndex\x12+\n\x11\x62inary_entrypoint\x18\x05 \x01(\tR\x10\x62inaryEntrypoint\x12\x36\n\x06inputs\x18\x06 \x03(\x0b\x32\x1e.sf.substreams.v1.Module.InputR\x06inputs\x12\x37\n\x06output\x18\x07 \x01(\x0b\x32\x1f.sf.substreams.v1.Module.OutputR\x06output\x12#\n\rinitial_block\x18\x08 \x01(\x04R\x0cinitialBlock\x1a*\n\x07KindMap\x12\x1f\n\x0boutput_type\x18\x01 \x01(\tR\noutputType\x1a\xc5\x02\n\tKindStore\x12T\n\rupdate_policy\x18\x01 \x01(\x0e\x32/.sf.substreams.v1.Module.KindStore.UpdatePolicyR\x0cupdatePolicy\x12\x1d\n\nvalue_type\x18\x02 \x01(\tR\tvalueType\"\xc2\x01\n\x0cUpdatePolicy\x12\x17\n\x13UPDATE_POLICY_UNSET\x10\x00\x12\x15\n\x11UPDATE_POLICY_SET\x10\x01\x12#\n\x1fUPDATE_POLICY_SET_IF_NOT_EXISTS\x10\x02\x12\x15\n\x11UPDATE_POLICY_ADD\x10\x03\x12\x15\n\x11UPDATE_POLICY_MIN\x10\x04\x12\x15\n\x11UPDATE_POLICY_MAX\x10\x05\x12\x18\n\x14UPDATE_POLICY_APPEND\x10\x06\x1a\x9f\x03\n\x05Input\x12?\n\x06source\x18\x01 \x01(\x0b\x32%.sf.substreams.v1.Module.Input.SourceH\x00R\x06source\x12\x36\n\x03map\x18\x02 \x01(\x0b\x32\".sf.substreams.v1.Module.Input.MapH\x00R\x03map\x12<\n\x05store\x18\x03 \x01(\x0b\x32$.sf.substreams.v1.Module.Input.StoreH\x00R\x05store\x1a\x1c\n\x06Source\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x1a&\n\x03Map\x12\x1f\n\x0bmodule_name\x18\x01 \x01(\tR\nmoduleName\x1a\x8f\x01\n\x05Store\x12\x1f\n\x0bmodule_name\x18\x01 \x01(\tR\nmoduleName\x12=\n\x04mode\x18\x02 \x01(\x0e\x32).sf.substreams.v1.Module.Input.Store.ModeR\x04mode\"&\n\x04Mode\x12\t\n\x05UNSET\x10\x00\x12\x07\n\x03GET\x10\x01\x12\n\n\x06\x44\x45LTAS\x10\x02\x42\x07\n\x05input\x1a\x1c\n\x06Output\x12\x12\n\x04type\x18\x01 \x01(\tR\x04typeB\x06\n\x04kindBFZDgithub.com/streamingfast/substreams/pb/sf/substreams/v1;pbsubstreamsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sf.substreams.v1.modules_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZDgithub.com/streamingfast/substreams/pb/sf/substreams/v1;pbsubstreams'
  _MODULES._serialized_start=52
  _MODULES._serialized_end=167
  _BINARY._serialized_start=169
  _BINARY._serialized_end=223
  _MODULE._serialized_start=226
  _MODULE._serialized_end=1444
  _MODULE_KINDMAP._serialized_start=618
  _MODULE_KINDMAP._serialized_end=660
  _MODULE_KINDSTORE._serialized_start=663
  _MODULE_KINDSTORE._serialized_end=988
  _MODULE_KINDSTORE_UPDATEPOLICY._serialized_start=794
  _MODULE_KINDSTORE_UPDATEPOLICY._serialized_end=988
  _MODULE_INPUT._serialized_start=991
  _MODULE_INPUT._serialized_end=1406
  _MODULE_INPUT_SOURCE._serialized_start=1183
  _MODULE_INPUT_SOURCE._serialized_end=1211
  _MODULE_INPUT_MAP._serialized_start=1213
  _MODULE_INPUT_MAP._serialized_end=1251
  _MODULE_INPUT_STORE._serialized_start=1254
  _MODULE_INPUT_STORE._serialized_end=1397
  _MODULE_INPUT_STORE_MODE._serialized_start=1359
  _MODULE_INPUT_STORE_MODE._serialized_end=1397
  _MODULE_OUTPUT._serialized_start=1408
  _MODULE_OUTPUT._serialized_end=1436
# @@protoc_insertion_point(module_scope)
