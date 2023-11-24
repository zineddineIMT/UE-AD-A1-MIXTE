import grpc
from concurrent import futures
import showtime_pb2
import showtime_pb2_grpc
import json


class ShowtimeServicer(showtime_pb2_grpc.ShowtimeServicer):
    def __init__(self):
        with open("data/times.json", "r") as file:
            self.schedule = json.load(file)["schedule"]

    def GetAllShowtimes(self, request, context):
        for item in self.schedule:
            yield showtime_pb2.ScheduleItem(date=item["date"], movies=item["movies"])

    def GetMoviesByDate(self, request, context):
        matching_schedule = next((item for item in self.schedule if item["date"] == request.date), None)
        if matching_schedule:
            return showtime_pb2.ScheduleItem(date=matching_schedule["date"], movies=matching_schedule["movies"])
        context.abort(grpc.StatusCode.NOT_FOUND, "No showtimes found for this date")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    showtime_pb2_grpc.add_ShowtimeServicer_to_server(ShowtimeServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    print("gRPC Server started, listening on port 3002")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
