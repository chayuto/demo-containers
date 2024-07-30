import socket
import time
import os
import random

def start_client(server_host='echo_server', server_port=5000):
    tcp_payload_size = int(os.getenv('TCP_PAYLOAD_SIZE', '1024'))
    interval_sec = int(os.getenv('INTERVAL_SEC', '5'))
    # Check if TCP_HOSTNAME environment variable is set and use it if available
    server_host = os.getenv('TCP_HOSTNAME', server_host)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    print(f"Connected to server at {server_host}:{server_port}", flush=True)

    while True:
        message = bytes(random.getrandbits(8) for _ in range(tcp_payload_size))
        client_socket.sendall(message)
        print(f"Sent {len(message)} bytes", flush=True)
        
        total_data = []
        bytes_recd = 0
        while bytes_recd < tcp_payload_size:
            data = client_socket.recv(min(tcp_payload_size - bytes_recd, 4096))
            if not data:
                break
            total_data.append(data)
            bytes_recd += len(data)
        
        print(f"Received {bytes_recd} bytes", flush=True)
        time.sleep(interval_sec)

    client_socket.close()

if __name__ == "__main__":
    start_client()
