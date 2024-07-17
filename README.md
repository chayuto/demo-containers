# demo-containers
 Demo container for testing and instrumentation


```bash
docker-compose up --build
```

```log
echo_server-1  | Echo server started on 0.0.0.0:5000
client-1       | Connected to server at echo_server:5000
client-1       | Received: Hello, Server!
echo_server-1  | Connection from ('172.19.0.3', 40432)
echo_server-1  | Received: Hello, Server!
echo_server-1  | Received: Hello, Server!
client-1       | Received: Hello, Server!
```