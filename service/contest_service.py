from proto import contest_pb2
from proto import contest_pb2_grpc
from util.data import contest_cache

class Contest(contest_pb2_grpc.ContestDataServiceServicer):

    def GetContestData(self, request, context):
        data = contest_cache[request.platform].get(request.handle)
        return contest_pb2.ContestData(
            handle = data['handle'],
            profile_url = data['profile_url'],
            contests = data['data']
        )


# def Contestserve():
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     contest_pb2_grpc.add_ContestDataServiceServicer_to_server(Contest(), server)
#     server.add_insecure_port('[::]:50051')
#     server.start()
#     server.wait_for_termination()