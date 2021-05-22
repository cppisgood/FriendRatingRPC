from proto import submit_pb2
from proto import submit_pb2_grpc
from util.data import submit_cache

class Submit(submit_pb2_grpc.SubmitDataServiceServicer):

    def GetSubmitData(self, request, context):
        data = submit_cache[request.platform].get(request.handle)
        return submit_pb2.SubmitData(
            handle = data['handle'],
            profile_url = data['profile_url'],
            accept_count = data['accept_count'],
            submit_count = data['submit_count'],
            data = data['data']
        )