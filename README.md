# CMPE273


# Assignment 1

Requirements

You will be implementing a dynamic Python invoker REST service. The service will have the following features:

1. Python Script Uploader

POST http://localhost:8000/api/v1/scripts
Request

foo.py

# foo.py
print("Hello World")
curl -i -X POST -H "Content-Type: multipart/form-data" 
-F "data=@/tmp/foo.py" http://localhost:8000/api/v1/scripts
201 Created
{
    "script-id": "123456"
}
2. Python Script Invoker

GET http://localhost:8000/api/v1/scripts/{script-id}
Request

curl -i
http://localhost:8000/api/v1/scripts/123456
200 OK
Hello World
