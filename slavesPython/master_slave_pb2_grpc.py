# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import master_slave_pb2 as master__slave__pb2


class MasterSlaveServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterSlave = channel.unary_unary(
                '/master_slave.MasterSlaveService/RegisterSlave',
                request_serializer=master__slave__pb2.SlaveInfo.SerializeToString,
                response_deserializer=master__slave__pb2.RegistrationResponse.FromString,
                )
        self.SendResult = channel.unary_unary(
                '/master_slave.MasterSlaveService/SendResult',
                request_serializer=master__slave__pb2.Result.SerializeToString,
                response_deserializer=master__slave__pb2.Acknowledgement.FromString,
                )


class MasterSlaveServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterSlave(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MasterSlaveServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterSlave': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterSlave,
                    request_deserializer=master__slave__pb2.SlaveInfo.FromString,
                    response_serializer=master__slave__pb2.RegistrationResponse.SerializeToString,
            ),
            'SendResult': grpc.unary_unary_rpc_method_handler(
                    servicer.SendResult,
                    request_deserializer=master__slave__pb2.Result.FromString,
                    response_serializer=master__slave__pb2.Acknowledgement.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'master_slave.MasterSlaveService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MasterSlaveService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterSlave(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/master_slave.MasterSlaveService/RegisterSlave',
            master__slave__pb2.SlaveInfo.SerializeToString,
            master__slave__pb2.RegistrationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/master_slave.MasterSlaveService/SendResult',
            master__slave__pb2.Result.SerializeToString,
            master__slave__pb2.Acknowledgement.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)