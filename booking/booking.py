import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc
import json

class BookingServicer(booking_pb2_grpc.BookingServicer):

    def __init__(self):
        with open('{}/data/bookings.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["bookings"]

    def GetAllBookings(self, request, context):
        for booking in self.db:
            yield booking_pb2.BookingItem(
                user_id=booking["userid"],
                movies=[booking_pb2.Date(date=date["date"], movie_ids=date["movies"]) for date in booking["dates"]]
            )

    def GetBookingsByUser(self, request, context):
        for booking in self.db:
            if booking["userid"] == request.user_id:
                yield booking_pb2.BookingItem(
                    user_id=booking["userid"],
                    movies=[booking_pb2.Date(date=date["date"], movie_ids=date["movies"]) for date in booking["dates"]]
                )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3003')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
