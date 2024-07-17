import socket

def start_echo_server(host='0.0.0.0', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Echo server started on {host}:{port}")
    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")
    
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode()}")
        conn.sendall(data)
    
    conn.close()
    server_socket.close()
    print("Server closed")

if __name__ == "__main__":
    start_echo_server()
