# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import showtime_pb2 as showtime__pb2


class ShowtimeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllShowtimes = channel.unary_stream(
                '/Showtime/GetAllShowtimes',
                request_serializer=showtime__pb2.EmptySchedule.SerializeToString,
                response_deserializer=showtime__pb2.ScheduleItem.FromString,
                )
        self.GetMoviesByDate = channel.unary_unary(
                '/Showtime/GetMoviesByDate',
                request_serializer=showtime__pb2.Date.SerializeToString,
                response_deserializer=showtime__pb2.ScheduleItem.FromString,
                )


class ShowtimeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllShowtimes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMoviesByDate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ShowtimeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllShowtimes': grpc.unary_stream_rpc_method_handler(
                    servicer.GetAllShowtimes,
                    request_deserializer=showtime__pb2.EmptySchedule.FromString,
                    response_serializer=showtime__pb2.ScheduleItem.SerializeToString,
            ),
            'GetMoviesByDate': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMoviesByDate,
                    request_deserializer=showtime__pb2.Date.FromString,
                    response_serializer=showtime__pb2.ScheduleItem.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Showtime', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Showtime(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllShowtimes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Showtime/GetAllShowtimes',
            showtime__pb2.EmptySchedule.SerializeToString,
            showtime__pb2.ScheduleItem.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMoviesByDate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Showtime/GetMoviesByDate',
            showtime__pb2.Date.SerializeToString,
            showtime__pb2.ScheduleItem.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
