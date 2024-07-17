import socket
import time

def start_client(server_host='echo_server', server_port=5000, message='Hello, Server!'):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    print(f"Connected to server at {server_host}:{server_port}")
    
    while True:
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")
        time.sleep(5)
    
    client_socket.close()

if __name__ == "__main__":
    start_client()
