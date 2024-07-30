
# Kubernetes deployment flavour

##  TCP Echo demo 
```
kubectl apply -f echo_server-service.yaml
kubectl apply -f echo_server-deployment.yaml
kubectl apply -f client-deployment.yaml
kubectl get pods
```

```
NAME                          READY   STATUS    RESTARTS      AGE
client-5fcc7fc88c-ljwqh       1/1     Running   1 (6s ago)    7s
echo-server-bfc9d64bb-5xcgl   1/1     Running   1 (74s ago)   17m
```