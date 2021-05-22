from logging import debug
from proto import contest_pb2
from proto import contest_pb2_grpc
from util.data import contest_cache

class Contest(contest_pb2_grpc.ContestDataServiceServicer):
    
    def GetContestData(self, request, context):
        data = contest_cache[request.platform].get(request.handle)
        return contest_pb2.ContestData(
            handle = data['handle'],
            profile_url = data['profile_url'],
            rating = data['rating'],
            length = data['length'],
            data = data['data']
        )