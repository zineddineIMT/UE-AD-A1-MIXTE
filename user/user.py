from flask import Flask, render_template, request, jsonify, make_response
import requests
import grpc
from google.protobuf.json_format import MessageToJson

import booking_pb2
import booking_pb2_grpc
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3203
HOST = '0.0.0.0'

with open('{}/data/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the User service!</h1>", 200)

@app.route("/users/<userId>/bookings", methods=['GET'])
def getUserBookings(userId):
    with grpc.insecure_channel('localhost:3003') as channel:  # Remplacer par l'adresse du service Booking
        booking_client = booking_pb2_grpc.BookingStub(channel)

        try:
            booking_response = booking_client.GetBookingsByUser(booking_pb2.UserId(userid=userId))

            booking_response_json = MessageToJson(booking_response)
            booking_response_data = json.loads(booking_response_json)

            print(booking_response_data)

            bookings = [{"userid": booking['userid'], "dates": booking['movies']} for booking in booking_response_data]
            return jsonify(bookings), 200
        except grpc.RpcError as e:
            return jsonify({"error": str(e)}), 500

@app.route("/users/<userId>/bookings/movies", methods=['GET'])
def getUserBookingMovies(userId):
    with grpc.insecure_channel('localhost:3002') as channel:  # Remplacer par l'adresse du service Booking
        booking_client = booking_pb2_grpc.BookingStub(channel)

        try:
            # Appel au service Booking
            response = booking_client.GetBookingsByUser(booking_pb2.UserId(user_id=userId))
            movie_details = []

            # URL de base du service Movie GraphQL
            movie_service_url = "http://127.0.0.1:3001/graphql"

            for booking in response:
                for date in booking.dates:
                    for movie_id in date.movie_ids:

                        # Construction de la requête GraphQL
                        graphql_query = """
                            query getMovieById($movieId: String!) {
                                movie_by_id(id: $movieId) {
                                    id
                                    title
                                    director
                                    rating
                                }
                            }
                        """
                        variables = {"movieId": movie_id}

                        # Appel au service Movie pour chaque ID de film
                        movie_response = requests.post(
                            movie_service_url,
                            json={'query': graphql_query, 'variables': variables}
                        )
                        if movie_response.status_code == 200:
                            movie_details.append(movie_response.json()['data']['movie_by_id'])

            return jsonify(movie_details), 200
        except grpc.RpcError as e:
            return jsonify({"error": str(e)}), 500

@app.route("/users/<userId>/bookings/add", methods=['POST'])
def addBookingForUser(userId):
    # Récupérer les données de la requête entrante
    booking_data = request.get_json()

    with grpc.insecure_channel('localhost:3002') as channel:  # Remplacer par l'adresse du service Booking
        booking_client = booking_pb2_grpc.BookingStub(channel)

        try:
            # Créer une requête gRPC avec les données reçues
            create_booking_request = booking_pb2.CreateBookingRequest(
                userid=userId,
                date=booking_data['date'],
                movieid=booking_data['movie_id']
            )

            # Envoyer la requête au service Booking
            response = booking_client.CreateBooking(create_booking_request)

            if response.error:
                # Gérer les erreurs possibles du service Booking
                return jsonify({"error": response.error}), 400
            else:
                return jsonify({"message": "Booking added successfully"}), 200

        except grpc.RpcError as e:
            # Gérer les erreurs de connexion au service Booking
            return jsonify({"error": "Failed to connect to Booking service", "details": str(e)}), 500

if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)