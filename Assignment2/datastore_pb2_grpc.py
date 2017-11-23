# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import datastore_pb2 as datastore__pb2


class DatastoreStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.message = channel.unary_stream(
        '/Datastore/message',
        request_serializer=datastore__pb2.Request.SerializeToString,
        response_deserializer=datastore__pb2.Response.FromString,
        )
    self.put = channel.unary_unary(
        '/Datastore/put',
        request_serializer=datastore__pb2.PutData.SerializeToString,
        response_deserializer=datastore__pb2.Empty.FromString,
        )
    self.delete = channel.unary_unary(
        '/Datastore/delete',
        request_serializer=datastore__pb2.DeleteData.SerializeToString,
        response_deserializer=datastore__pb2.Empty.FromString,
        )
    self.get_db = channel.unary_unary(
        '/Datastore/get_db',
        request_serializer=datastore__pb2.Empty.SerializeToString,
        response_deserializer=datastore__pb2.getData.FromString,
        )


class DatastoreServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def message(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def put(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def get_db(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DatastoreServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'message': grpc.unary_stream_rpc_method_handler(
          servicer.message,
          request_deserializer=datastore__pb2.Request.FromString,
          response_serializer=datastore__pb2.Response.SerializeToString,
      ),
      'put': grpc.unary_unary_rpc_method_handler(
          servicer.put,
          request_deserializer=datastore__pb2.PutData.FromString,
          response_serializer=datastore__pb2.Empty.SerializeToString,
      ),
      'delete': grpc.unary_unary_rpc_method_handler(
          servicer.delete,
          request_deserializer=datastore__pb2.DeleteData.FromString,
          response_serializer=datastore__pb2.Empty.SerializeToString,
      ),
      'get_db': grpc.unary_unary_rpc_method_handler(
          servicer.get_db,
          request_deserializer=datastore__pb2.Empty.FromString,
          response_serializer=datastore__pb2.getData.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Datastore', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
