'''
################################## server.py #############################
#
################################## server.py #############################
'''
import time
import grpc
import datastore_pb2
import datastore_pb2_grpc
import rocksdb
import queue

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class MyDatastoreServicer(datastore_pb2.DatastoreServicer):
    

    def __init__(self):
        print("started init....")
        self.db = rocksdb.DB("master.db", rocksdb.Options(create_if_missing=True))
        self.new_queue = queue.Queue()


    def message(self, request, context):
        print("Slave connected")
        while True:
            new_operation = self.new_queue.get()
            yield new_operation


    def put_slave(f):
        def wrapper(self, request, context):
            msg = datastore_pb2.Response(
                    operation="put",
                    key= request.key,
                    data=request.data
                 ) 
            self.new_queue.put(msg)
            return f(self, request, context)
        return wrapper

    def delete_slave(f):
        def wrapper(self, request, context):
            msg = datastore_pb2.Response( 
                    operation="delete",
                    key= request.key,
                    data = "none"
                 ) 
            self.new_queue.put(msg)
            return f(self, request, context)
        return wrapper

    @put_slave
    def put(self, request, context):
        print("put " +request.key + " " + request.data + " from master db to slave")
        key = request.key
        data = request.data
        self.db.put(key.encode(), data.encode()) #put in master db
        return datastore_pb2.Operation_Response(data = "done")

    @delete_slave
    def delete(self, request, context):
        print("Delete "+ request.key +" key from master db to slave")
        key = request.key
        self.db.delete(key.encode()) #delete from master db
        return datastore_pb2.Operation_Response(data = "done")

def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    datastore_pb2_grpc.add_DatastoreServicer_to_server(MyDatastoreServicer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()

    try:
        while True:
            print("Server started at...%d" % port)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    print("... here ...")
    run('0.0.0.0', 3000)
