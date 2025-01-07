import socket
import struct
import time
import random
import threading
import subprocess
import sctp
from project_messages_pb2 import conn_req, conn_resp, netstat_req, netstat_resp, netstat_data, netmeas_req, netmeas_resp, netmeas_data, hello

# Constants
tcp_server_ip = "10.64.45.4"
tcp_server_port = 65432
sctp_server_ip = "127.0.0.1"
sctp_server_port = 54322
team_id = 5  # Your team ID

def send_message(client_socket, message):
    serialized_data = message.SerializeToString()
    client_socket.send(len(serialized_data).to_bytes(4, 'big'))
    client_socket.sendall(serialized_data)
    message_name = type(message).__name__
    print(f"[SEND] {message_name}: {message}")

def receive_message(client_socket, message_type):
    try:
        data_length = int.from_bytes(client_socket.recv(4), 'big')
        data = client_socket.recv(data_length)
        message = message_type()
        message.ParseFromString(data)
        print(f"[RECEIVE] {message_type.__name__}: {message}")
        return message
    except socket.timeout:
        print(f"[TIMEOUT] No response received for {message_type.__name__}")
        return None

def send_conn_req(client_socket):
    message = conn_req()
    message.header.id = team_id
    student = message.student.add()
    student.aem = 2572
    student.name = "Daniil Mavroudis"
    student.email = "example@domain.com"
    send_message(client_socket, message)

def handle_conn_resp(client_socket):
    return receive_message(client_socket, conn_resp)

def send_netstat_req(client_socket):
    message = netstat_req()
    message.header.id = team_id
    send_message(client_socket, message)

def handle_netstat_resp(client_socket):
    return receive_message(client_socket, netstat_resp)

def send_netstat_data(client_socket):
    message = netstat_data()
    message.header.id = team_id
    message.ip_address = "192.168.1.1"
    message.mac_address = "00:1A:2B:3C:4D:5E"
    send_message(client_socket, message)

def send_netmeas_req(client_socket):
    message = netmeas_req()
    message.header.id = team_id
    send_message(client_socket, message)

def handle_netmeas_resp(client_socket):
    return receive_message(client_socket, netmeas_resp)

def send_netmeas_report(client_socket, bandwidth):
    message = netmeas_data()
    message.header.id = team_id
    message.report = bandwidth
    send_message(client_socket, message)

def run_iperf3(server_ip, port, interval):
    try:
        result = subprocess.run([
            "iperf3", "-c", server_ip, "-p", str(port), "-t", str(interval), "--json"
        ], capture_output=True, text=True, check=True)
        print("iperf3 output:", result.stdout)
        import json
        iperf_data = json.loads(result.stdout)
        bandwidth = iperf_data['end']['sum_received']['bits_per_second'] / 1e6  # Mbps
        print(f"[IPERF3] Bandwidth: {bandwidth} Mbps")
        return bandwidth
    except subprocess.CalledProcessError as e:
        print("[IPERF3 ERROR]:", e.stderr)
        return 0

def tcp_communication():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_client:
        tcp_client.settimeout(30)  # Increased timeout for debugging
        print("[TCP] Connecting to server...")
        tcp_client.connect((tcp_server_ip, tcp_server_port))
        print("[TCP] Connected.")

        send_conn_req(tcp_client)
        conn_response = handle_conn_resp(tcp_client)
        if not conn_response:
            return

        send_netstat_req(tcp_client)
        netstat_response = handle_netstat_resp(tcp_client)
        if not netstat_response:
            return

        send_netstat_data(tcp_client)

        send_netmeas_req(tcp_client)
        netmeas_response = handle_netmeas_resp(tcp_client)
        if not netmeas_response:
            return

        bandwidth = run_iperf3(tcp_server_ip, netmeas_response.port, netmeas_response.interval)
        send_netmeas_report(tcp_client, bandwidth)

def send_hello_messages():
    sctp_client = sctp.sctpsocket_tcp(socket.AF_INET)
    try:
        print("[SCTP] Connecting to server...")
        sctp_client.connect((sctp_server_ip, sctp_server_port))
        print("[SCTP] Connected.")

        while True:
            hello_msg = hello()
            hello_msg.header.id = team_id
            hello_msg.header.type = 1  # Explicitly setting the type for HELLO
            serialized_data = hello_msg.SerializeToString()
            sctp_client.send(len(serialized_data).to_bytes(4, 'big') + serialized_data)
            print(f"[SEND] HELLO: {hello_msg}")
            time.sleep(random.randint(5, 10))
    except Exception as e:
        print(f"[SCTP ERROR] {e}")
    finally:
        sctp_client.close()

def sctp_communication():
    threading.Thread(target=send_hello_messages, daemon=True).start()

if __name__ == "__main__":
    threading.Thread(target=tcp_communication).start()
    sctp_communication()


