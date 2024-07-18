import socket
from datetime import datetime

def log_with_timestamp(message):
    print(f"{datetime.now().isoformat()} - {message}", flush=True)

def start_udp_server(host='0.0.0.0', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    log_with_timestamp(f"UDP server started on {host}:{port}")
    
    while True:
        data, addr = server_socket.recvfrom(4096)
        log_with_timestamp(f"Received {len(data)} bytes from {addr}")
    
    server_socket.close()
    log_with_timestamp("Server closed")

if __name__ == "__main__":
    start_udp_server()