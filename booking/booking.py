import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc

import showtime_pb2
import showtime_pb2_grpc

import json

class BookingServicer(booking_pb2_grpc.BookingServicer):

    def __init__(self):
        with open('{}/data/bookings.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["bookings"]

    def GetAllBookings(self, request, context):
        for booking in self.db:
            yield booking_pb2.BookingItem(
                userid=booking["userid"],
                movies=[booking_pb2.Date(date=date["date"], movies=date["movies"]) for date in booking["dates"]]
            )

    def GetBookingsByUser(self, request, context):
        for booking in self.db:
            if booking["userid"] == request.userid:
                yield booking_pb2.BookingItem(
                    userid=booking["userid"],
                    movies=[booking_pb2.Date(date=date["date"], movies=date["movies"]) for date in booking["dates"]]
                )

    def CreateBooking(self, request, context):
        # Établir la connexion avec le service Showtime
        with grpc.insecure_channel('localhost:3002') as channel:  # Remplacer par l'adresse du service Showtime
            showtime_client = showtime_pb2_grpc.ShowtimeStub(channel)

            # Préparer la requête pour le service Showtime
            showtime_request = showtime_client.GetMoviesByDate(booking_pb2.Date(date = request.date))

            # Appeler le service Showtime pour vérifier la disponibilité du film
            try:
                showtime_response = showtime_client.GetMoviesByDate(showtime_request)
                print(showtime_response)
                if request.movie_id not in showtime_response.movies:
                    return booking_pb2.CreateBookingResponse(
                        booking=None,
                        error="Movie not available on this date"
                    )
            except grpc.RpcError as e:
                # Gérer l'erreur RPC
                return booking_pb2.CreateBookingResponse(
                    booking=None,
                    error=f"Failed to connect to Showtime service: {e}"
                )

        # Vérifier si l'utilisateur et la date existent déjà dans les réservations
        user_found = False
        date_found = False
        for booking in self.db:
            if booking['userid'] == request.userid:
                user_found = True
                for movie_date in booking['dates']:
                    if movie_date['date'] == request.date:
                        date_found = True
                        # Ajouter le movie_id à la liste existante
                        movie_date['movies'].append(request.movie_id)
                        break
                if not date_found:
                    # Créer une nouvelle entrée de date
                    booking['dates'].append({
                        "date": request.date,
                        "movies": [request.movie_id]
                    })
                break

        if not user_found:
            # Créer une nouvelle réservation pour un nouvel utilisateur
            self.db.append({
                "userid": request.userid,
                "movies": [{
                    "date": request.date,
                    "movies": [request.movie_id]
                }]
            })

        # Créer une réponse avec les détails de la réservation
        return booking_pb2.CreateBookingResponse(
            booking=booking_pb2.BookingItem(
                userid=request.userid,
                movies=[booking_pb2.Date(date=request.date, movies=[request.movie_id])]
            )
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3003')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
