## Assignment 2



## 1. Run Master

```bash
docker run -p 3000:3000 -it -- --name lab1-server -v "$PWD":/usr/src/myapp -w /usr/src/myapp ubuntu-python3.6-rocksdb-grpc:1.0 python3.6 server.py

```


## 2. Run Slave 

```bash
docker run -it --rm --name lab1-client1 -v "$PWD":/usr/src/myapp -w /usr/src/myapp ubuntu-python3.6-rocksdb-grpc:1.0 python3.6 client.py 192.168.0.1

```

## 3. Run TestClient

```bash
docker run -it --rm --name lab1-client2 -v "$PWD":/usr/src/myapp -w /usr/src/myapp ubuntu-python3.6-rocksdb-grpc:1.0 python3.6 TestClient.py 192.168.0.1
```
