'''
################################## client.py #############################
# 
################################## client.py #############################
'''
import time
import grpc
import datastore_pb2
import datastore_pb2_grpc
import argparse
import rocksdb

from concurrent import futures

PORT = 3000

class Client():
    
    def __init__(self, host='0.0.0.0', port=PORT):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2.DatastoreStub(self.channel)
        self.testdb = rocksdb.DB("slave.db", rocksdb.Options(create_if_missing=True))
        self.replication()

    #sync with server database(replication)
    def replication(self):
       print("inside connect function.....")
       response_stream = self.stub.message(datastore_pb2.Request(data="send message")) 
       for response in response_stream:
            if response.operation == "put":
                print("response addition of : " + response.key+", " + response.data) 
                #inserts value inside slave database
                self.testdb.put(response.key.encode('utf-8'), response.data.encode('utf-8')) 
            elif response.operation == "delete":
                print("response deletion of : "+ response.key)
                #delete the key from slave database
                self.testdb.put(response.key.encode('utf-8'), response.data.encode('utf-8')) 
            else:
                pass
        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="abcd")
    args = parser.parse_args()
    print("Client is connecting to Server at {}:{}...".format(args.host, PORT))
    client = Client(host=args.host)

if __name__ == "__main__":
    main()
