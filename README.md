# gRPC-python
gRPC-python example code

1. Python 環境安裝
```
pip install grpcio grpcio-tools
```

2. 檔案生成
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. greeter.proto
```