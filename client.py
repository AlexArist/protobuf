import socket
import time
import struct
import threading
import subprocess
import json
import logging
from sctp import sctpsocket_tcp
import project_messages_pb2 as pb

# Configure Logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("Client")

TEAM_ID = 5
TCP_IP = "10.64.45.4"
SCTP_IP = "127.0.0.1"
TCP_PORT = 65432
SCTP_PORT = 54322

# Sender and Receiver methods
def send_msg(sock, msg):
    try:
        data = msg.SerializeToString()
        length = len(data)
        sock.sendall(length.to_bytes(4, 'big'))
        sock.sendall(data)
        logger.info(f"Sent message: {msg}")
    except Exception as e:
        logger.error(f"Failed to send message: {e}")

def receive_msg(sock):
    try:
        length_data = sock.recv(4)
        if not length_data:
            raise ConnectionError("Socket closed by server.")
        length = int.from_bytes(length_data, 'big')
        data = sock.recv(length)
        wrapper = pb.project_msg()
        wrapper.ParseFromString(data)

        # Return the content based on the message type
        if wrapper.HasField("conn_resp_msg"):
            return wrapper.conn_resp_msg
        elif wrapper.HasField("netstat_resp_msg"):
            return wrapper.netstat_resp_msg
        elif wrapper.HasField("netmeas_resp_msg"):
            return wrapper.netmeas_resp_msg
        elif wrapper.HasField("netmeas_data_ack_msg"):
            return wrapper.netmeas_data_ack_msg
        else:
            logger.warning("Unknown message type received.")
            return None
    except Exception as e:
        logger.error(f"Failed to receive message: {e}")
        return None

# Message Creation Handlers
def create_conn_req_msg(student_details):
    header = pb.ece441_header()
    header.id = TEAM_ID
    header.type = pb.ECE441_CONN_REQ
    conn_req = pb.conn_req()
    conn_req.header.CopyFrom(header)
    for student in student_details:
        person = conn_req.student.add()
        person.aem = student['aem']
        person.name = student['name']
        person.email = student['email']
    wrapper = pb.project_msg()
    wrapper.conn_req_msg.CopyFrom(conn_req)
    return wrapper

def create_hello_msg():
    header = pb.ece441_header()
    header.id = TEAM_ID
    header.type = pb.ECE441_HELLO
    hello_msg = pb.hello()
    hello_msg.header.CopyFrom(header)
    wrapper = pb.project_msg()
    wrapper.hello_msg.CopyFrom(hello_msg)
    return wrapper

def create_netstat_req_msg(student_details):
    header = pb.ece441_header()
    header.id = TEAM_ID
    header.type = pb.ECE441_NETSTAT_REQ
    netstat_req = pb.netstat_req()
    netstat_req.header.CopyFrom(header)
    for student in student_details:
        person = netstat_req.student.add()
        person.aem = student['aem']
        person.name = student['name']
        person.email = student['email']
    wrapper = pb.project_msg()
    wrapper.netstat_req_msg.CopyFrom(netstat_req)
    return wrapper

def create_netmeas_data_msg(report):
    header = pb.ece441_header()
    header.id = TEAM_ID
    header.type = pb.ECE441_NETMEAS_DATA
    netmeas_data = pb.netmeas_data()
    netmeas_data.header.CopyFrom(header)
    netmeas_data.report = report
    wrapper = pb.project_msg()
    wrapper.netmeas_data_msg.CopyFrom(netmeas_data)
    return wrapper

# HELLO Thread Handler
def hello_thread(sctp_sock, interval):
    last_send_time = 0
    while True:
        now = time.time()
        if now - last_send_time >= interval:
            hello_message = create_hello_msg()
            send_msg(sctp_sock, hello_message)
            logger.info("[HELLO] Sent HELLO message.")
            last_send_time = now
        time.sleep(0.3)

# Main Execution
if __name__ == "__main__":
    try:
        # TCP Connection
        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_sock.connect((TCP_IP, TCP_PORT))
        logger.info("[TCP] Connected.")

        students = [
            {"aem": 2572, "name": "Daniil Mavroudis", "email": "dmavroudis@uth.com"},
            {"aem": 2497, "name": "Konstantinos Vakalis", "email": "kvakalis@uth.com"},
            {"aem": 1414, "name": "Alexandros Aristeidou", "email": "aristeid@uth.com"},
            {"aem": 9494, "name": "Dimitris Revithis", "email": "drevithis@uth.com"}
        ]

        # CONN_REQ and CONN_RESP
        conn_req_message = create_conn_req_msg(students)
        send_msg(tcp_sock, conn_req_message)
        conn_resp_message = receive_msg(tcp_sock)
        if conn_resp_message is None:
            raise ValueError("No response for CONN_REQ.")
        interval = conn_resp_message.interval
        logger.info(f"[CONN_RESP] Received interval: {interval}.")

        # SCTP Connection
        sctp_sock = sctpsocket_tcp(socket.AF_INET)
        sctp_sock.connect((SCTP_IP, SCTP_PORT))
        logger.info("[SCTP] Connected.")

        # Start HELLO Thread
        threading.Thread(target=hello_thread, args=(sctp_sock, interval), daemon=True).start()

        # NETSTAT_REQ and NETSTAT_RESP
        netstat_req_message = create_netstat_req_msg(students)
        send_msg(tcp_sock, netstat_req_message)
        netstat_resp_message = receive_msg(tcp_sock)
        logger.info("[NETSTAT_RESP] Received NETSTAT response.")

        # iperf3 Throughput Test
        result = subprocess.run(
            ["iperf3", "-c", TCP_IP, "-p", str(5201), "-t", str(interval), "--json"],
            capture_output=True, text=True, check=True
        )
        bandwidth = json.loads(result.stdout)['end']['sum_received']['bits_per_second'] / 1e6
        logger.info(f"[IPERF3] Bandwidth: {bandwidth:.2f} Mbps.")

        # NETMEAS_DATA and NETMEAS_DATA_ACK
        netmeas_data_message = create_netmeas_data_msg(bandwidth)
        send_msg(tcp_sock, netmeas_data_message)
        netmeas_data_ack_message = receive_msg(tcp_sock)
        logger.info("[NETMEAS_DATA_ACK] Received NETMEAS data acknowledgment.")

    except Exception as e:
        logger.error(f"Error occurred: {e}")

    finally:
        # Cleanup
        tcp_sock.close()
        sctp_sock.close()
        logger.info("All connections closed.")
