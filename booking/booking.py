import grpc
from concurrent import futures

from google.protobuf.json_format import MessageToJson

import booking_pb2
import booking_pb2_grpc

import showtime_pb2
import showtime_pb2_grpc

import json
from datetime import datetime


class BookingServicer(booking_pb2_grpc.BookingServicer):

    def __init__(self):
        with open('{}/data/bookings.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["bookings"]

    def GetAllBookings(self, request, context):
        for booking in self.db:
            yield booking_pb2.BookingItem(
                userid=booking["userid"],
                dates=[booking_pb2.Date(date=date["date"], movies=date["movies"]) for date in booking["dates"]]
            )

    def GetBookingsByUser(self, request, context):
        for booking in self.db:
            if booking["userid"] == request.userid:
                yield booking_pb2.BookingItem(
                    userid=booking["userid"],
                    dates=[booking_pb2.Date(date=date["date"], movies=date["movies"]) for date in booking["dates"]]
                )

    def CreateBooking(self, request, context):

        # Vérifie si les champs nécessaires sont présents dans les données de réservation
        if not request or not request.date or not request.movieid:
            return booking_pb2.CreateBookingResponse(
                booking=None,
                error="Invalid data format"
            )

        # Vérifie le format de la date
        try:
            datetime.strptime(request.date, '%Y%m%d')
        except ValueError:
            return booking_pb2.CreateBookingResponse(
                booking=None,
                error="Invalid date format"
            )

        # Établir la connexion avec le service Showtime
        with grpc.insecure_channel('localhost:3002') as channel:  # Remplacer par l'adresse du service Showtime
            showtime_client = showtime_pb2_grpc.ShowtimeStub(channel)


            # Appeler le service Showtime pour vérifier la disponibilité du film
            try:
                showtime_response = showtime_client.GetMoviesByDate(booking_pb2.Date(date=request.date))

                showtime_response_json = MessageToJson(showtime_response)
                showtime_response_data = json.loads(showtime_response_json)

                if request.movieid not in showtime_response_data['movies']:
                    return booking_pb2.CreateBookingResponse(
                        booking=None,
                        error="Movie not available on this date"
                    )
            except grpc.RpcError as e:
                # Gérer l'erreur RPC
                return booking_pb2.CreateBookingResponse(
                    booking=None,
                    error="Failed to connect to Showtime service: "
                )

        date_already_booked = False

        for booking in self.db:
            if booking['userid'] == request.userid:
                for d in booking['dates']:
                    if d['date'] == request.date:
                        date_already_booked = True
                        if request.movieid in d['movies']:
                            return booking_pb2.CreateBookingResponse(
                                booking=None,
                                error="An existing item already exists "
                            )
        # Ajoute la réservation pour un utilisateur existant ou crée une nouvelle entrée pour un nouvel utilisateur
        new_booking = {"date": request.date, "movies": [request.movieid]}
        existing_user_book = next((b for b in self.db if b["userid"] == request.userid), None)
        existing_user_dates = existing_user_book['dates']
        if existing_user_book:
            if date_already_booked:
                existing_user_dates[0]['movies'].append(request.movieid)
            else:
                existing_user_dates.append(new_booking)
        else:
            self.db.append({"userid": request.userid, "dates": [new_booking]})

        return booking_pb2.CreateBookingResponse(
            booking=booking_pb2.BookingItem(userid=request.userid, dates=[new_booking]),
            error=""
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3003')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
