# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project_messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16project_messages.proto\"Q\n\rece441_header\x12\x0f\n\x02id\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x1f\n\x04type\x18\x02 \x01(\x0e\x32\x0c.ece441_typeH\x01\x88\x01\x01\x42\x05\n\x03_idB\x07\n\x05_type\"9\n\rece441_person\x12\x0b\n\x03\x61\x65m\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"K\n\x08\x63onn_req\x12\x1e\n\x06header\x18\x01 \x01(\x0b\x32\x0e.ece441_header\x12\x1f\n\x07student\x18\x02 \x03(\x0b\x32\x0e.ece441_person\"\'\n\x05hello\x12\x1e\n\x06header\x18\x01 \x01(\x0b\x32\x0e.ece441_header\"\x88\x01\n\tconn_resp\x12\x1e\n\x06header\x18\x01 \x01(\x0b\x32\x0e.ece441_header\x12)\n\tdirection\x18\x02 \x01(\x0e\x32\x11.ece441_directionH\x00\x88\x01\x01\x12\x15\n\x08interval\x18\x03 \x01(\rH\x01\x88\x01\x01\x42\x0c\n\n_directionB\x0b\n\t_interval\"N\n\x0bnetstat_req\x12\x1e\n\x06header\x18\x01 \x01(\x0b\x32\x0e.ece441_header\x12\x1f\n\x07student\x18\x02 \x03(\x0b\x32\x0e.ece441_person\"g\n\x0cnetstat_resp\x12\x1e\n\x06header\x18\x01 \x01(\x0b\x32\x0e.ece441_header\x12)\n\tdirection\x18\x02 \x01(\x0e\x32\x11.ece441_directionH\x00\x88\x01\x01\x42\x0c\n\n_direction\"\x80\x01\n\x0cnetstat_data\x12\x1e\n\x06header\x18\x01 \x01(\x0b\x32\x0e.ece441_header\x12\x18\n\x0bmac_address\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nip_address\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x0e\n\x0c_mac_addressB\r\n\x0b_ip_address\"k\n\x10netstat_data_ack\x12\x1e\n\x06header\x18\x01 \x01(\x0b\x32\x0e.ece441_header\x12)\n\tdirection\x18\x02 \x01(\x0e\x32\x11.ece441_directionH\x00\x88\x01\x01\x42\x0c\n\n_direction\"N\n\x0bnetmeas_req\x12\x1e\n\x06header\x18\x01 \x01(\x0b\x32\x0e.ece441_header\x12\x1f\n\x07student\x18\x02 \x03(\x0b\x32\x0e.ece441_person\"\xa7\x01\n\x0cnetmeas_resp\x12\x1e\n\x06header\x18\x01 \x01(\x0b\x32\x0e.ece441_header\x12)\n\tdirection\x18\x02 \x01(\x0e\x32\x11.ece441_directionH\x00\x88\x01\x01\x12\x15\n\x08interval\x18\x03 \x01(\rH\x01\x88\x01\x01\x12\x11\n\x04port\x18\x04 \x01(\rH\x02\x88\x01\x01\x42\x0c\n\n_directionB\x0b\n\t_intervalB\x07\n\x05_port\"\x87\x01\n\x0cnetmeas_data\x12\x1e\n\x06header\x18\x01 \x01(\x0b\x32\x0e.ece441_header\x12)\n\tdirection\x18\x02 \x01(\x0e\x32\x11.ece441_directionH\x00\x88\x01\x01\x12\x13\n\x06report\x18\x03 \x01(\x02H\x01\x88\x01\x01\x42\x0c\n\n_directionB\t\n\x07_report\"k\n\x10netmeas_data_ack\x12\x1e\n\x06header\x18\x01 \x01(\x0b\x32\x0e.ece441_header\x12)\n\tdirection\x18\x02 \x01(\x0e\x32\x11.ece441_directionH\x00\x88\x01\x01\x42\x0c\n\n_direction\"\xd9\x03\n\x0bproject_msg\x12\x1b\n\thello_msg\x18\x01 \x01(\x0b\x32\x06.helloH\x00\x12!\n\x0c\x63onn_req_msg\x18\x02 \x01(\x0b\x32\t.conn_reqH\x00\x12#\n\rconn_resp_msg\x18\x03 \x01(\x0b\x32\n.conn_respH\x00\x12\'\n\x0fnetstat_req_msg\x18\x04 \x01(\x0b\x32\x0c.netstat_reqH\x00\x12)\n\x10netstat_resp_msg\x18\x05 \x01(\x0b\x32\r.netstat_respH\x00\x12)\n\x10netstat_data_msg\x18\x06 \x01(\x0b\x32\r.netstat_dataH\x00\x12\x31\n\x14netstat_data_ack_msg\x18\x07 \x01(\x0b\x32\x11.netstat_data_ackH\x00\x12\'\n\x0fnetmeas_req_msg\x18\x08 \x01(\x0b\x32\x0c.netmeas_reqH\x00\x12)\n\x10netmeas_resp_msg\x18\t \x01(\x0b\x32\r.netmeas_respH\x00\x12)\n\x10netmeas_data_msg\x18\n \x01(\x0b\x32\r.netmeas_dataH\x00\x12-\n\x10netmeas_data_ack\x18\x0b \x01(\x0b\x32\x11.netmeas_data_ackH\x00\x42\x05\n\x03msg*\x98\x02\n\x0b\x65\x63\x65\x34\x34\x31_type\x12\x10\n\x0c\x45\x43\x45\x34\x34\x31_HELLO\x10\x00\x12\x13\n\x0f\x45\x43\x45\x34\x34\x31_CONN_REQ\x10\x01\x12\x14\n\x10\x45\x43\x45\x34\x34\x31_CONN_RESP\x10\x02\x12\x16\n\x12\x45\x43\x45\x34\x34\x31_NETSTAT_REQ\x10\x03\x12\x17\n\x13\x45\x43\x45\x34\x34\x31_NETSTAT_RESP\x10\x04\x12\x17\n\x13\x45\x43\x45\x34\x34\x31_NETSTAT_DATA\x10\x05\x12\x1b\n\x17\x45\x43\x45\x34\x34\x31_NETSTAT_DATA_ACK\x10\x06\x12\x16\n\x12\x45\x43\x45\x34\x34\x31_NETMEAS_REQ\x10\x07\x12\x17\n\x13\x45\x43\x45\x34\x34\x31_NETMEAS_RESP\x10\x08\x12\x17\n\x13\x45\x43\x45\x34\x34\x31_NETMEAS_DATA\x10\t\x12\x1b\n\x17\x45\x43\x45\x34\x34\x31_NETMEAS_DATA_ACK\x10\n*A\n\x10\x65\x63\x65\x34\x34\x31_direction\x12\x0b\n\x07NOT_SET\x10\x00\x12\x0e\n\nSUCCESSFUL\x10\x01\x12\x10\n\x0cUNSUCCESSFUL\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'project_messages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ECE441_TYPE._serialized_start=1824
  _ECE441_TYPE._serialized_end=2104
  _ECE441_DIRECTION._serialized_start=2106
  _ECE441_DIRECTION._serialized_end=2171
  _ECE441_HEADER._serialized_start=26
  _ECE441_HEADER._serialized_end=107
  _ECE441_PERSON._serialized_start=109
  _ECE441_PERSON._serialized_end=166
  _CONN_REQ._serialized_start=168
  _CONN_REQ._serialized_end=243
  _HELLO._serialized_start=245
  _HELLO._serialized_end=284
  _CONN_RESP._serialized_start=287
  _CONN_RESP._serialized_end=423
  _NETSTAT_REQ._serialized_start=425
  _NETSTAT_REQ._serialized_end=503
  _NETSTAT_RESP._serialized_start=505
  _NETSTAT_RESP._serialized_end=608
  _NETSTAT_DATA._serialized_start=611
  _NETSTAT_DATA._serialized_end=739
  _NETSTAT_DATA_ACK._serialized_start=741
  _NETSTAT_DATA_ACK._serialized_end=848
  _NETMEAS_REQ._serialized_start=850
  _NETMEAS_REQ._serialized_end=928
  _NETMEAS_RESP._serialized_start=931
  _NETMEAS_RESP._serialized_end=1098
  _NETMEAS_DATA._serialized_start=1101
  _NETMEAS_DATA._serialized_end=1236
  _NETMEAS_DATA_ACK._serialized_start=1238
  _NETMEAS_DATA_ACK._serialized_end=1345
  _PROJECT_MSG._serialized_start=1348
  _PROJECT_MSG._serialized_end=1821
# @@protoc_insertion_point(module_scope)
