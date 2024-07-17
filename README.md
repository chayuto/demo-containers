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
docker-compose up --build
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
