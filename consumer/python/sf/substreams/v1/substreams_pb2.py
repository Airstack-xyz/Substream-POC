# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sf/substreams/v1/substreams.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from sf.substreams.v1 import modules_pb2 as sf_dot_substreams_dot_v1_dot_modules__pb2
from sf.substreams.v1 import clock_pb2 as sf_dot_substreams_dot_v1_dot_clock__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!sf/substreams/v1/substreams.proto\x12\x10sf.substreams.v1\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1esf/substreams/v1/modules.proto\x1a\x1csf/substreams/v1/clock.proto\"\x9a\x03\n\x07Request\x12&\n\x0fstart_block_num\x18\x01 \x01(\x03R\rstartBlockNum\x12!\n\x0cstart_cursor\x18\x02 \x01(\tR\x0bstartCursor\x12$\n\x0estop_block_num\x18\x03 \x01(\x04R\x0cstopBlockNum\x12\x39\n\nfork_steps\x18\x04 \x03(\x0e\x32\x1a.sf.substreams.v1.ForkStepR\tforkSteps\x12;\n\x19irreversibility_condition\x18\x05 \x01(\tR\x18irreversibilityCondition\x12\x33\n\x07modules\x18\x06 \x01(\x0b\x32\x19.sf.substreams.v1.ModulesR\x07modules\x12%\n\x0eoutput_modules\x18\x07 \x03(\tR\routputModules\x12J\n\"initial_store_snapshot_for_modules\x18\x08 \x03(\tR\x1einitialStoreSnapshotForModules\"\xb7\x02\n\x08Response\x12?\n\x08progress\x18\x01 \x01(\x0b\x32!.sf.substreams.v1.ModulesProgressH\x00R\x08progress\x12L\n\rsnapshot_data\x18\x02 \x01(\x0b\x32%.sf.substreams.v1.InitialSnapshotDataH\x00R\x0csnapshotData\x12X\n\x11snapshot_complete\x18\x03 \x01(\x0b\x32).sf.substreams.v1.InitialSnapshotCompleteH\x00R\x10snapshotComplete\x12\x37\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32!.sf.substreams.v1.BlockScopedDataH\x00R\x04\x64\x61taB\t\n\x07message\"1\n\x17InitialSnapshotComplete\x12\x16\n\x06\x63ursor\x18\x01 \x01(\tR\x06\x63ursor\"\xa9\x01\n\x13InitialSnapshotData\x12\x1f\n\x0bmodule_name\x18\x01 \x01(\tR\nmoduleName\x12\x35\n\x06\x64\x65ltas\x18\x02 \x01(\x0b\x32\x1d.sf.substreams.v1.StoreDeltasR\x06\x64\x65ltas\x12\x1b\n\tsent_keys\x18\x04 \x01(\x04R\x08sentKeys\x12\x1d\n\ntotal_keys\x18\x03 \x01(\x04R\ttotalKeys\"\xc2\x01\n\x0f\x42lockScopedData\x12\x38\n\x07outputs\x18\x01 \x03(\x0b\x32\x1e.sf.substreams.v1.ModuleOutputR\x07outputs\x12-\n\x05\x63lock\x18\x03 \x01(\x0b\x32\x17.sf.substreams.v1.ClockR\x05\x63lock\x12.\n\x04step\x18\x06 \x01(\x0e\x32\x1a.sf.substreams.v1.ForkStepR\x04step\x12\x16\n\x06\x63ursor\x18\n \x01(\tR\x06\x63ursor\"\xe0\x01\n\x0cModuleOutput\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x35\n\nmap_output\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00R\tmapOutput\x12\x42\n\x0cstore_deltas\x18\x03 \x01(\x0b\x32\x1d.sf.substreams.v1.StoreDeltasH\x00R\x0bstoreDeltas\x12\x12\n\x04logs\x18\x04 \x03(\tR\x04logs\x12%\n\x0elogs_truncated\x18\x05 \x01(\x08R\rlogsTruncatedB\x06\n\x04\x64\x61ta\"M\n\x0fModulesProgress\x12:\n\x07modules\x18\x01 \x03(\x0b\x32 .sf.substreams.v1.ModuleProgressR\x07modules\"\xe6\x05\n\x0eModuleProgress\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\\\n\x10processed_ranges\x18\x02 \x01(\x0b\x32/.sf.substreams.v1.ModuleProgress.ProcessedRangeH\x00R\x0fprocessedRanges\x12T\n\rinitial_state\x18\x03 \x01(\x0b\x32-.sf.substreams.v1.ModuleProgress.InitialStateH\x00R\x0cinitialState\x12Z\n\x0fprocessed_bytes\x18\x04 \x01(\x0b\x32/.sf.substreams.v1.ModuleProgress.ProcessedBytesH\x00R\x0eprocessedBytes\x12\x41\n\x06\x66\x61iled\x18\x05 \x01(\x0b\x32\'.sf.substreams.v1.ModuleProgress.FailedH\x00R\x06\x66\x61iled\x1aY\n\x0eProcessedRange\x12G\n\x10processed_ranges\x18\x01 \x03(\x0b\x32\x1c.sf.substreams.v1.BlockRangeR\x0fprocessedRanges\x1a\x41\n\x0cInitialState\x12\x31\n\x15\x61vailable_up_to_block\x18\x02 \x01(\x04R\x12\x61vailableUpToBlock\x1aj\n\x0eProcessedBytes\x12(\n\x10total_bytes_read\x18\x01 \x01(\x04R\x0etotalBytesRead\x12.\n\x13total_bytes_written\x18\x02 \x01(\x04R\x11totalBytesWritten\x1a[\n\x06\x46\x61iled\x12\x16\n\x06reason\x18\x01 \x01(\tR\x06reason\x12\x12\n\x04logs\x18\x02 \x03(\tR\x04logs\x12%\n\x0elogs_truncated\x18\x03 \x01(\x08R\rlogsTruncatedB\x06\n\x04type\"J\n\nBlockRange\x12\x1f\n\x0bstart_block\x18\x02 \x01(\x04R\nstartBlock\x12\x1b\n\tend_block\x18\x03 \x01(\x04R\x08\x65ndBlock\"C\n\x0bStoreDeltas\x12\x34\n\x06\x64\x65ltas\x18\x01 \x03(\x0b\x32\x1c.sf.substreams.v1.StoreDeltaR\x06\x64\x65ltas\"\xf4\x01\n\nStoreDelta\x12\x44\n\toperation\x18\x01 \x01(\x0e\x32&.sf.substreams.v1.StoreDelta.OperationR\toperation\x12\x18\n\x07ordinal\x18\x02 \x01(\x04R\x07ordinal\x12\x10\n\x03key\x18\x03 \x01(\tR\x03key\x12\x1b\n\told_value\x18\x04 \x01(\x0cR\x08oldValue\x12\x1b\n\tnew_value\x18\x05 \x01(\x0cR\x08newValue\":\n\tOperation\x12\t\n\x05UNSET\x10\x00\x12\n\n\x06\x43REATE\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\"\xa6\x01\n\x06Output\x12\x1b\n\tblock_num\x18\x01 \x01(\x04R\x08\x62lockNum\x12\x19\n\x08\x62lock_id\x18\x02 \x01(\tR\x07\x62lockId\x12\x38\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12*\n\x05value\x18\n \x01(\x0b\x32\x14.google.protobuf.AnyR\x05value*\\\n\x08\x46orkStep\x12\x10\n\x0cSTEP_UNKNOWN\x10\x00\x12\x0c\n\x08STEP_NEW\x10\x01\x12\r\n\tSTEP_UNDO\x10\x02\x12\x15\n\x11STEP_IRREVERSIBLE\x10\x04\"\x04\x08\x03\x10\x03\"\x04\x08\x05\x10\x05\x32K\n\x06Stream\x12\x41\n\x06\x42locks\x12\x19.sf.substreams.v1.Request\x1a\x1a.sf.substreams.v1.Response0\x01\x42\x46ZDgithub.com/streamingfast/substreams/pb/sf/substreams/v1;pbsubstreamsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sf.substreams.v1.substreams_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZDgithub.com/streamingfast/substreams/pb/sf/substreams/v1;pbsubstreams'
  _FORKSTEP._serialized_start=2936
  _FORKSTEP._serialized_end=3028
  _REQUEST._serialized_start=178
  _REQUEST._serialized_end=588
  _RESPONSE._serialized_start=591
  _RESPONSE._serialized_end=902
  _INITIALSNAPSHOTCOMPLETE._serialized_start=904
  _INITIALSNAPSHOTCOMPLETE._serialized_end=953
  _INITIALSNAPSHOTDATA._serialized_start=956
  _INITIALSNAPSHOTDATA._serialized_end=1125
  _BLOCKSCOPEDDATA._serialized_start=1128
  _BLOCKSCOPEDDATA._serialized_end=1322
  _MODULEOUTPUT._serialized_start=1325
  _MODULEOUTPUT._serialized_end=1549
  _MODULESPROGRESS._serialized_start=1551
  _MODULESPROGRESS._serialized_end=1628
  _MODULEPROGRESS._serialized_start=1631
  _MODULEPROGRESS._serialized_end=2373
  _MODULEPROGRESS_PROCESSEDRANGE._serialized_start=2008
  _MODULEPROGRESS_PROCESSEDRANGE._serialized_end=2097
  _MODULEPROGRESS_INITIALSTATE._serialized_start=2099
  _MODULEPROGRESS_INITIALSTATE._serialized_end=2164
  _MODULEPROGRESS_PROCESSEDBYTES._serialized_start=2166
  _MODULEPROGRESS_PROCESSEDBYTES._serialized_end=2272
  _MODULEPROGRESS_FAILED._serialized_start=2274
  _MODULEPROGRESS_FAILED._serialized_end=2365
  _BLOCKRANGE._serialized_start=2375
  _BLOCKRANGE._serialized_end=2449
  _STOREDELTAS._serialized_start=2451
  _STOREDELTAS._serialized_end=2518
  _STOREDELTA._serialized_start=2521
  _STOREDELTA._serialized_end=2765
  _STOREDELTA_OPERATION._serialized_start=2707
  _STOREDELTA_OPERATION._serialized_end=2765
  _OUTPUT._serialized_start=2768
  _OUTPUT._serialized_end=2934
  _STREAM._serialized_start=3030
  _STREAM._serialized_end=3105
# @@protoc_insertion_point(module_scope)
