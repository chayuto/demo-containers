# Demo Containers
Collection of demo container/use-case for testing and instrumentation


## TCP Echo Server and Client

This project contains a simple TCP Echo Server and Client implemented in Python, running in Docker containers and managed by Docker Compose. The client sends random bytes of a specified size to the server, which echoes them back.

```
├── echo_server
│ ├── Dockerfile
│ └── echo_server.py
├── tcp_client
│ ├── Dockerfile
│ └── client.py
└── docker-compose.yml
└── README.md
```

### echo_server

This directory contains the echo server implementation.

- `echo_server.py`: A simple TCP echo server that receives data and sends it back to the client.
- `Dockerfile`: Dockerfile for building the echo server container.

### tcp_client

This directory contains the client implementation.

- `client.py`: A simple TCP client that sends random bytes of a specified size to the server and prints the number of bytes received.
- `Dockerfile`: Dockerfile for building the client container.


```bash
docker compose up --build
```

Environment Variables
The client can be configured using the following environment variables:

TCP_PAYLOAD_SIZE: The size of the payload (in bytes) to be sent by the client. Default is 1024.

INTERVAL_SEC: The interval (in seconds) between each send operation. Default is 5.

Server:
```log
Echo server started on 0.0.0.0:5000
Connection from ('172.18.0.2', 34567)
Received 1024 bytes
Received 1024 bytes
...
Server closed
```


Client:
```
Connected to server at echo_server:5000
Sent 1024 bytes
Received 1024 bytes
Sent 1024 bytes
Received 1024 bytes
...
```


## UDP test
This project contains a simple UDP Server and Client. The client sends random bytes of a specified size to the server, which logs them with timestamps.

```
├── udp_server
│   ├── Dockerfile
│   └── udp_server.py
├── udp_client
│   ├── Dockerfile
│   └── udp_client.py
└── docker-compose-udp.yml
```

```
docker compose -f docker-compose-udp.yaml up --build
```

## Flask POST file Server 

```bash
sudo docker compose -f flask_post_server/docker-compose.yaml up --build
```


```bash
curl -X POST http://localhost:5000/receive -F "file=@flask_post_server/test_file.txt"
```

example response:
```log
flask_server-1  | Received a POST request
flask_server-1  | Processing file: file
flask_server-1  | Request Metadata:
flask_server-1  | remote_addr: 192.168.65.1
flask_server-1  | method: POST
flask_server-1  | url: http://localhost:5000/receive
flask_server-1  | base_url: http://localhost:5000/receive
flask_server-1  | url_root: http://localhost:5000/
flask_server-1  | headers: {'Host': 'localhost:5000', 'User-Agent': 'curl/8.6.0', 'Accept': '*/*', 'Content-Length': '209', 'Content-Type': 'multipart/form-data; boundary=------------------------PRFY7fg7KRYeroulwPwXgP'}
flask_server-1  | form: {}
flask_server-1  | args: {}
flask_server-1  | files: {'file': {'length': 6, 'content': b'Potato'}}
flask_server-1  | File: file, Length: 6
flask_server-1  | Content: b'Potato'
flask_server-1  | 192.168.65.1 - - [25/Jul/2024 02:11:02] "POST /receive HTTP/1.1" 200 -
```