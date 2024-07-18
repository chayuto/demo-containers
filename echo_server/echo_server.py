import socket
from datetime import datetime

def log_with_timestamp(message):
    print(f"{datetime.now().isoformat()} - {message}", flush=True)

def start_echo_server(host='0.0.0.0', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    log_with_timestamp(f"Echo server started on {host}:{port}")
    conn, addr = server_socket.accept()
    log_with_timestamp(f"Connection from {addr}")
    
    while True:
        data = conn.recv(4096)
        if not data:
            break
        log_with_timestamp(f"Received {len(data)} bytes")
        conn.sendall(data)
    
    conn.close()
    server_socket.close()
    log_with_timestamp("Server closed")

if __name__ == "__main__":
    start_echo_server()
