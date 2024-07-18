import socket
import time
import os
import random
from datetime import datetime

def log_with_timestamp(message):
    print(f"{datetime.now().isoformat()} - {message}", flush=True)

def start_udp_client(server_host='udp_server', server_port=5000):
    tcp_payload_size = int(os.getenv('PAYLOAD_SIZE', '1024'))
    interval_sec = int(os.getenv('INTERVAL_SEC', '5'))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (server_host, server_port)
    log_with_timestamp(f"UDP client started, sending to {server_host}:{server_port}")

    while True:
        message = bytes(random.getrandbits(8) for _ in range(tcp_payload_size))
        client_socket.sendto(message, server_address)
        log_with_timestamp(f"Sent {len(message)} bytes")
        time.sleep(interval_sec)

    client_socket.close()

if __name__ == "__main__":
    start_udp_client()
