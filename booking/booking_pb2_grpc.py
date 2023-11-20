# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import booking_pb2 as booking__pb2


class BookingStub(object):
    """Le service gérant les réservations.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllBookings = channel.unary_stream(
                '/booking.Booking/GetAllBookings',
                request_serializer=booking__pb2.Empty.SerializeToString,
                response_deserializer=booking__pb2.BookingItem.FromString,
                )
        self.GetBookingsByUser = channel.unary_stream(
                '/booking.Booking/GetBookingsByUser',
                request_serializer=booking__pb2.UserId.SerializeToString,
                response_deserializer=booking__pb2.BookingItem.FromString,
                )


class BookingServicer(object):
    """Le service gérant les réservations.
    """

    def GetAllBookings(self, request, context):
        """RPC pour obtenir la liste complète des réservations.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBookingsByUser(self, request, context):
        """RPC pour obtenir les réservations d'un utilisateur spécifique.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllBookings': grpc.unary_stream_rpc_method_handler(
                    servicer.GetAllBookings,
                    request_deserializer=booking__pb2.Empty.FromString,
                    response_serializer=booking__pb2.BookingItem.SerializeToString,
            ),
            'GetBookingsByUser': grpc.unary_stream_rpc_method_handler(
                    servicer.GetBookingsByUser,
                    request_deserializer=booking__pb2.UserId.FromString,
                    response_serializer=booking__pb2.BookingItem.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'booking.Booking', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Booking(object):
    """Le service gérant les réservations.
    """

    @staticmethod
    def GetAllBookings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/booking.Booking/GetAllBookings',
            booking__pb2.Empty.SerializeToString,
            booking__pb2.BookingItem.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBookingsByUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/booking.Booking/GetBookingsByUser',
            booking__pb2.UserId.SerializeToString,
            booking__pb2.BookingItem.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)