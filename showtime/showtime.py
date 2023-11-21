import grpc
from concurrent import futures
import showtime_pb2
import showtime_pb2_grpc
import json

class ShowtimeServicer(showtime_pb2_grpc.ShowtimeServicer):

    def __init__(self):
        with open('{}/data/times.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["schedule"]

    def GetAllShowtimes(self, request, context):
        for showtime in self.db:
            yield showtime_pb2.Schedule(date=showtime["date"], movies=showtime["movies"])

    def GetMoviesByDate(self, request, context):
        for showtime in self.db:
            if showtime["date"] == request.date:
                # Créer et renvoyer un objet Schedule avec la date et les IDs de films
                return showtime_pb2.Schedule(date=showtime["date"], movies=showtime["movies"])

        # Si aucune correspondance n'est trouvée, renvoyer un objet Schedule vide
        return showtime_pb2.Schedule()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    showtime_pb2_grpc.add_ShowtimeServicer_to_server(ShowtimeServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
