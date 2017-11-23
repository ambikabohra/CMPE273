import argparse
import grpc
import datastore_pb2


PORT = 3000

class TestClient():
    def __init__(self, host='0.0.0.0', port=PORT):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2.DatastoreStub(self.channel)

    def put(self, key, data):
        return self.stub.put(datastore_pb2.PutData(key=key, data=data))

    def delete(self, key):
        return self.stub.delete(datastore_pb2.DeleteData(key=key))

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="abcd")
    args = parser.parse_args()
    print("Client is connecting to Server at {}:{}...".format(args.host, PORT))
    test = TestClient(host=args.host)

    print('Test 1: put function : key = key1 and value = Arya')
    test.put("key1","Arya")

    print("Test 2: put function : key = key2 and value = Parth")
    test.put("key2","Parth")
    
    print("Test 4: delete function : key = key1 " )
    test.delete("key1")

    print("Test 1: put function : key = key3 and value = Rachit")
    test.put("key3", "Rachit")

    

if __name__ == "__main__":
    main()