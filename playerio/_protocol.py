# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: playerio.proto

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
  name='playerio.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0eplayerio.proto\"\xf8\x01\n\x14SimpleConnectRequest\x12\x0f\n\x07game_id\x18\x01 \x01(\t\x12\x19\n\x11username_or_email\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x1f\n\x17player_insight_segments\x18\x04 \x03(\t\x12\x12\n\nclient_api\x18\x05 \x01(\t\x12:\n\x0b\x63lient_info\x18\x06 \x03(\x0b\x32%.SimpleConnectRequest.ClientInfoEntry\x1a\x31\n\x0f\x43lientInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x92\x01\n\x12PlayerInsightState\x12\x16\n\x0eplayers_online\x18\x01 \x01(\x05\x12\x33\n\x08segments\x18\x02 \x03(\x0b\x32!.PlayerInsightState.SegmentsEntry\x1a/\n\rSegmentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb1\x01\n\x13SimpleConnectOutput\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x15\n\rshow_branding\x18\x03 \x01(\x08\x12\x1c\n\x14game_fs_redirect_map\x18\x04 \x01(\t\x12\x12\n\npartner_id\x18\x05 \x01(\t\x12\x31\n\x14player_insight_state\x18\x06 \x01(\x0b\x32\x13.PlayerInsightState\"3\n\x12SimpleConnectError\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"\xd3\x01\n\x10ListRoomsRequest\x12\x11\n\troom_type\x18\x01 \x01(\t\x12>\n\x0fsearch_criteria\x18\x02 \x03(\x0b\x32%.ListRoomsRequest.SearchCriteriaEntry\x12\r\n\x05limit\x18\x03 \x01(\x05\x12\x0e\n\x06offset\x18\x04 \x01(\x05\x12\x16\n\x0eonly_dev_rooms\x18\x05 \x01(\x08\x1a\x35\n\x13SearchCriteriaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8a\x01\n\x08RoomInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x14\n\x0conline_users\x18\x03 \x01(\x05\x12!\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x13.RoomInfo.DataEntry\x1a+\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"+\n\x0fListRoomsOutput\x12\x18\n\x05rooms\x18\x01 \x03(\x0b\x32\t.RoomInfo\"/\n\x0eListRoomsError\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"\xb5\x02\n\x15\x43reateJoinRoomRequest\x12\x0f\n\x07room_id\x18\x01 \x01(\t\x12\x11\n\troom_type\x18\x02 \x01(\t\x12\x0f\n\x07visible\x18\x03 \x01(\x08\x12\x37\n\troom_data\x18\x04 \x03(\x0b\x32$.CreateJoinRoomRequest.RoomDataEntry\x12\x37\n\tjoin_data\x18\x05 \x03(\x0b\x32$.CreateJoinRoomRequest.JoinDataEntry\x12\x13\n\x0bis_dev_room\x18\x06 \x01(\x08\x1a/\n\rRoomDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rJoinDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"/\n\x0eServerEndpoint\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"X\n\x14\x43reateJoinRoomOutput\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08join_key\x18\x02 \x01(\t\x12\"\n\tendpoints\x18\x03 \x03(\x0b\x32\x0f.ServerEndpoint\"4\n\x13\x43reateJoinRoomError\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SIMPLECONNECTREQUEST_CLIENTINFOENTRY = _descriptor.Descriptor(
  name='ClientInfoEntry',
  full_name='SimpleConnectRequest.ClientInfoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='SimpleConnectRequest.ClientInfoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='SimpleConnectRequest.ClientInfoEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=267,
)

_SIMPLECONNECTREQUEST = _descriptor.Descriptor(
  name='SimpleConnectRequest',
  full_name='SimpleConnectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_id', full_name='SimpleConnectRequest.game_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='username_or_email', full_name='SimpleConnectRequest.username_or_email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='SimpleConnectRequest.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_insight_segments', full_name='SimpleConnectRequest.player_insight_segments', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_api', full_name='SimpleConnectRequest.client_api', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_info', full_name='SimpleConnectRequest.client_info', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SIMPLECONNECTREQUEST_CLIENTINFOENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=267,
)


_PLAYERINSIGHTSTATE_SEGMENTSENTRY = _descriptor.Descriptor(
  name='SegmentsEntry',
  full_name='PlayerInsightState.SegmentsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PlayerInsightState.SegmentsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='PlayerInsightState.SegmentsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=369,
  serialized_end=416,
)

_PLAYERINSIGHTSTATE = _descriptor.Descriptor(
  name='PlayerInsightState',
  full_name='PlayerInsightState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='players_online', full_name='PlayerInsightState.players_online', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='segments', full_name='PlayerInsightState.segments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PLAYERINSIGHTSTATE_SEGMENTSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=270,
  serialized_end=416,
)


_SIMPLECONNECTOUTPUT = _descriptor.Descriptor(
  name='SimpleConnectOutput',
  full_name='SimpleConnectOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='SimpleConnectOutput.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SimpleConnectOutput.user_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='show_branding', full_name='SimpleConnectOutput.show_branding', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_fs_redirect_map', full_name='SimpleConnectOutput.game_fs_redirect_map', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='partner_id', full_name='SimpleConnectOutput.partner_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_insight_state', full_name='SimpleConnectOutput.player_insight_state', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=419,
  serialized_end=596,
)


_SIMPLECONNECTERROR = _descriptor.Descriptor(
  name='SimpleConnectError',
  full_name='SimpleConnectError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='SimpleConnectError.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='SimpleConnectError.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=598,
  serialized_end=649,
)


_LISTROOMSREQUEST_SEARCHCRITERIAENTRY = _descriptor.Descriptor(
  name='SearchCriteriaEntry',
  full_name='ListRoomsRequest.SearchCriteriaEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ListRoomsRequest.SearchCriteriaEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ListRoomsRequest.SearchCriteriaEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=810,
  serialized_end=863,
)

_LISTROOMSREQUEST = _descriptor.Descriptor(
  name='ListRoomsRequest',
  full_name='ListRoomsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='room_type', full_name='ListRoomsRequest.room_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search_criteria', full_name='ListRoomsRequest.search_criteria', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit', full_name='ListRoomsRequest.limit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='ListRoomsRequest.offset', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='only_dev_rooms', full_name='ListRoomsRequest.only_dev_rooms', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_LISTROOMSREQUEST_SEARCHCRITERIAENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=652,
  serialized_end=863,
)


_ROOMINFO_DATAENTRY = _descriptor.Descriptor(
  name='DataEntry',
  full_name='RoomInfo.DataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='RoomInfo.DataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='RoomInfo.DataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=961,
  serialized_end=1004,
)

_ROOMINFO = _descriptor.Descriptor(
  name='RoomInfo',
  full_name='RoomInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='RoomInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='RoomInfo.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='online_users', full_name='RoomInfo.online_users', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='RoomInfo.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ROOMINFO_DATAENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=866,
  serialized_end=1004,
)


_LISTROOMSOUTPUT = _descriptor.Descriptor(
  name='ListRoomsOutput',
  full_name='ListRoomsOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rooms', full_name='ListRoomsOutput.rooms', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1006,
  serialized_end=1049,
)


_LISTROOMSERROR = _descriptor.Descriptor(
  name='ListRoomsError',
  full_name='ListRoomsError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='ListRoomsError.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='ListRoomsError.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1051,
  serialized_end=1098,
)


_CREATEJOINROOMREQUEST_ROOMDATAENTRY = _descriptor.Descriptor(
  name='RoomDataEntry',
  full_name='CreateJoinRoomRequest.RoomDataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='CreateJoinRoomRequest.RoomDataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='CreateJoinRoomRequest.RoomDataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1314,
  serialized_end=1361,
)

_CREATEJOINROOMREQUEST_JOINDATAENTRY = _descriptor.Descriptor(
  name='JoinDataEntry',
  full_name='CreateJoinRoomRequest.JoinDataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='CreateJoinRoomRequest.JoinDataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='CreateJoinRoomRequest.JoinDataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1363,
  serialized_end=1410,
)

_CREATEJOINROOMREQUEST = _descriptor.Descriptor(
  name='CreateJoinRoomRequest',
  full_name='CreateJoinRoomRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='room_id', full_name='CreateJoinRoomRequest.room_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='room_type', full_name='CreateJoinRoomRequest.room_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visible', full_name='CreateJoinRoomRequest.visible', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='room_data', full_name='CreateJoinRoomRequest.room_data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='join_data', full_name='CreateJoinRoomRequest.join_data', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_dev_room', full_name='CreateJoinRoomRequest.is_dev_room', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CREATEJOINROOMREQUEST_ROOMDATAENTRY, _CREATEJOINROOMREQUEST_JOINDATAENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1101,
  serialized_end=1410,
)


_SERVERENDPOINT = _descriptor.Descriptor(
  name='ServerEndpoint',
  full_name='ServerEndpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='ServerEndpoint.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='ServerEndpoint.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1412,
  serialized_end=1459,
)


_CREATEJOINROOMOUTPUT = _descriptor.Descriptor(
  name='CreateJoinRoomOutput',
  full_name='CreateJoinRoomOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CreateJoinRoomOutput.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='join_key', full_name='CreateJoinRoomOutput.join_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='endpoints', full_name='CreateJoinRoomOutput.endpoints', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1461,
  serialized_end=1549,
)


_CREATEJOINROOMERROR = _descriptor.Descriptor(
  name='CreateJoinRoomError',
  full_name='CreateJoinRoomError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='CreateJoinRoomError.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='CreateJoinRoomError.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1551,
  serialized_end=1603,
)

_SIMPLECONNECTREQUEST_CLIENTINFOENTRY.containing_type = _SIMPLECONNECTREQUEST
_SIMPLECONNECTREQUEST.fields_by_name['client_info'].message_type = _SIMPLECONNECTREQUEST_CLIENTINFOENTRY
_PLAYERINSIGHTSTATE_SEGMENTSENTRY.containing_type = _PLAYERINSIGHTSTATE
_PLAYERINSIGHTSTATE.fields_by_name['segments'].message_type = _PLAYERINSIGHTSTATE_SEGMENTSENTRY
_SIMPLECONNECTOUTPUT.fields_by_name['player_insight_state'].message_type = _PLAYERINSIGHTSTATE
_LISTROOMSREQUEST_SEARCHCRITERIAENTRY.containing_type = _LISTROOMSREQUEST
_LISTROOMSREQUEST.fields_by_name['search_criteria'].message_type = _LISTROOMSREQUEST_SEARCHCRITERIAENTRY
_ROOMINFO_DATAENTRY.containing_type = _ROOMINFO
_ROOMINFO.fields_by_name['data'].message_type = _ROOMINFO_DATAENTRY
_LISTROOMSOUTPUT.fields_by_name['rooms'].message_type = _ROOMINFO
_CREATEJOINROOMREQUEST_ROOMDATAENTRY.containing_type = _CREATEJOINROOMREQUEST
_CREATEJOINROOMREQUEST_JOINDATAENTRY.containing_type = _CREATEJOINROOMREQUEST
_CREATEJOINROOMREQUEST.fields_by_name['room_data'].message_type = _CREATEJOINROOMREQUEST_ROOMDATAENTRY
_CREATEJOINROOMREQUEST.fields_by_name['join_data'].message_type = _CREATEJOINROOMREQUEST_JOINDATAENTRY
_CREATEJOINROOMOUTPUT.fields_by_name['endpoints'].message_type = _SERVERENDPOINT
DESCRIPTOR.message_types_by_name['SimpleConnectRequest'] = _SIMPLECONNECTREQUEST
DESCRIPTOR.message_types_by_name['PlayerInsightState'] = _PLAYERINSIGHTSTATE
DESCRIPTOR.message_types_by_name['SimpleConnectOutput'] = _SIMPLECONNECTOUTPUT
DESCRIPTOR.message_types_by_name['SimpleConnectError'] = _SIMPLECONNECTERROR
DESCRIPTOR.message_types_by_name['ListRoomsRequest'] = _LISTROOMSREQUEST
DESCRIPTOR.message_types_by_name['RoomInfo'] = _ROOMINFO
DESCRIPTOR.message_types_by_name['ListRoomsOutput'] = _LISTROOMSOUTPUT
DESCRIPTOR.message_types_by_name['ListRoomsError'] = _LISTROOMSERROR
DESCRIPTOR.message_types_by_name['CreateJoinRoomRequest'] = _CREATEJOINROOMREQUEST
DESCRIPTOR.message_types_by_name['ServerEndpoint'] = _SERVERENDPOINT
DESCRIPTOR.message_types_by_name['CreateJoinRoomOutput'] = _CREATEJOINROOMOUTPUT
DESCRIPTOR.message_types_by_name['CreateJoinRoomError'] = _CREATEJOINROOMERROR

SimpleConnectRequest = _reflection.GeneratedProtocolMessageType('SimpleConnectRequest', (_message.Message,), dict(

  ClientInfoEntry = _reflection.GeneratedProtocolMessageType('ClientInfoEntry', (_message.Message,), dict(
    DESCRIPTOR = _SIMPLECONNECTREQUEST_CLIENTINFOENTRY,
    __module__ = 'playerio_pb2'
    # @@protoc_insertion_point(class_scope:SimpleConnectRequest.ClientInfoEntry)
    ))
  ,
  DESCRIPTOR = _SIMPLECONNECTREQUEST,
  __module__ = 'playerio_pb2'
  # @@protoc_insertion_point(class_scope:SimpleConnectRequest)
  ))
_sym_db.RegisterMessage(SimpleConnectRequest)
_sym_db.RegisterMessage(SimpleConnectRequest.ClientInfoEntry)

PlayerInsightState = _reflection.GeneratedProtocolMessageType('PlayerInsightState', (_message.Message,), dict(

  SegmentsEntry = _reflection.GeneratedProtocolMessageType('SegmentsEntry', (_message.Message,), dict(
    DESCRIPTOR = _PLAYERINSIGHTSTATE_SEGMENTSENTRY,
    __module__ = 'playerio_pb2'
    # @@protoc_insertion_point(class_scope:PlayerInsightState.SegmentsEntry)
    ))
  ,
  DESCRIPTOR = _PLAYERINSIGHTSTATE,
  __module__ = 'playerio_pb2'
  # @@protoc_insertion_point(class_scope:PlayerInsightState)
  ))
_sym_db.RegisterMessage(PlayerInsightState)
_sym_db.RegisterMessage(PlayerInsightState.SegmentsEntry)

SimpleConnectOutput = _reflection.GeneratedProtocolMessageType('SimpleConnectOutput', (_message.Message,), dict(
  DESCRIPTOR = _SIMPLECONNECTOUTPUT,
  __module__ = 'playerio_pb2'
  # @@protoc_insertion_point(class_scope:SimpleConnectOutput)
  ))
_sym_db.RegisterMessage(SimpleConnectOutput)

SimpleConnectError = _reflection.GeneratedProtocolMessageType('SimpleConnectError', (_message.Message,), dict(
  DESCRIPTOR = _SIMPLECONNECTERROR,
  __module__ = 'playerio_pb2'
  # @@protoc_insertion_point(class_scope:SimpleConnectError)
  ))
_sym_db.RegisterMessage(SimpleConnectError)

ListRoomsRequest = _reflection.GeneratedProtocolMessageType('ListRoomsRequest', (_message.Message,), dict(

  SearchCriteriaEntry = _reflection.GeneratedProtocolMessageType('SearchCriteriaEntry', (_message.Message,), dict(
    DESCRIPTOR = _LISTROOMSREQUEST_SEARCHCRITERIAENTRY,
    __module__ = 'playerio_pb2'
    # @@protoc_insertion_point(class_scope:ListRoomsRequest.SearchCriteriaEntry)
    ))
  ,
  DESCRIPTOR = _LISTROOMSREQUEST,
  __module__ = 'playerio_pb2'
  # @@protoc_insertion_point(class_scope:ListRoomsRequest)
  ))
_sym_db.RegisterMessage(ListRoomsRequest)
_sym_db.RegisterMessage(ListRoomsRequest.SearchCriteriaEntry)

RoomInfo = _reflection.GeneratedProtocolMessageType('RoomInfo', (_message.Message,), dict(

  DataEntry = _reflection.GeneratedProtocolMessageType('DataEntry', (_message.Message,), dict(
    DESCRIPTOR = _ROOMINFO_DATAENTRY,
    __module__ = 'playerio_pb2'
    # @@protoc_insertion_point(class_scope:RoomInfo.DataEntry)
    ))
  ,
  DESCRIPTOR = _ROOMINFO,
  __module__ = 'playerio_pb2'
  # @@protoc_insertion_point(class_scope:RoomInfo)
  ))
_sym_db.RegisterMessage(RoomInfo)
_sym_db.RegisterMessage(RoomInfo.DataEntry)

ListRoomsOutput = _reflection.GeneratedProtocolMessageType('ListRoomsOutput', (_message.Message,), dict(
  DESCRIPTOR = _LISTROOMSOUTPUT,
  __module__ = 'playerio_pb2'
  # @@protoc_insertion_point(class_scope:ListRoomsOutput)
  ))
_sym_db.RegisterMessage(ListRoomsOutput)

ListRoomsError = _reflection.GeneratedProtocolMessageType('ListRoomsError', (_message.Message,), dict(
  DESCRIPTOR = _LISTROOMSERROR,
  __module__ = 'playerio_pb2'
  # @@protoc_insertion_point(class_scope:ListRoomsError)
  ))
_sym_db.RegisterMessage(ListRoomsError)

CreateJoinRoomRequest = _reflection.GeneratedProtocolMessageType('CreateJoinRoomRequest', (_message.Message,), dict(

  RoomDataEntry = _reflection.GeneratedProtocolMessageType('RoomDataEntry', (_message.Message,), dict(
    DESCRIPTOR = _CREATEJOINROOMREQUEST_ROOMDATAENTRY,
    __module__ = 'playerio_pb2'
    # @@protoc_insertion_point(class_scope:CreateJoinRoomRequest.RoomDataEntry)
    ))
  ,

  JoinDataEntry = _reflection.GeneratedProtocolMessageType('JoinDataEntry', (_message.Message,), dict(
    DESCRIPTOR = _CREATEJOINROOMREQUEST_JOINDATAENTRY,
    __module__ = 'playerio_pb2'
    # @@protoc_insertion_point(class_scope:CreateJoinRoomRequest.JoinDataEntry)
    ))
  ,
  DESCRIPTOR = _CREATEJOINROOMREQUEST,
  __module__ = 'playerio_pb2'
  # @@protoc_insertion_point(class_scope:CreateJoinRoomRequest)
  ))
_sym_db.RegisterMessage(CreateJoinRoomRequest)
_sym_db.RegisterMessage(CreateJoinRoomRequest.RoomDataEntry)
_sym_db.RegisterMessage(CreateJoinRoomRequest.JoinDataEntry)

ServerEndpoint = _reflection.GeneratedProtocolMessageType('ServerEndpoint', (_message.Message,), dict(
  DESCRIPTOR = _SERVERENDPOINT,
  __module__ = 'playerio_pb2'
  # @@protoc_insertion_point(class_scope:ServerEndpoint)
  ))
_sym_db.RegisterMessage(ServerEndpoint)

CreateJoinRoomOutput = _reflection.GeneratedProtocolMessageType('CreateJoinRoomOutput', (_message.Message,), dict(
  DESCRIPTOR = _CREATEJOINROOMOUTPUT,
  __module__ = 'playerio_pb2'
  # @@protoc_insertion_point(class_scope:CreateJoinRoomOutput)
  ))
_sym_db.RegisterMessage(CreateJoinRoomOutput)

CreateJoinRoomError = _reflection.GeneratedProtocolMessageType('CreateJoinRoomError', (_message.Message,), dict(
  DESCRIPTOR = _CREATEJOINROOMERROR,
  __module__ = 'playerio_pb2'
  # @@protoc_insertion_point(class_scope:CreateJoinRoomError)
  ))
_sym_db.RegisterMessage(CreateJoinRoomError)


_SIMPLECONNECTREQUEST_CLIENTINFOENTRY.has_options = True
_SIMPLECONNECTREQUEST_CLIENTINFOENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_PLAYERINSIGHTSTATE_SEGMENTSENTRY.has_options = True
_PLAYERINSIGHTSTATE_SEGMENTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_LISTROOMSREQUEST_SEARCHCRITERIAENTRY.has_options = True
_LISTROOMSREQUEST_SEARCHCRITERIAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_ROOMINFO_DATAENTRY.has_options = True
_ROOMINFO_DATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_CREATEJOINROOMREQUEST_ROOMDATAENTRY.has_options = True
_CREATEJOINROOMREQUEST_ROOMDATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_CREATEJOINROOMREQUEST_JOINDATAENTRY.has_options = True
_CREATEJOINROOMREQUEST_JOINDATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
