import logging
import grpc
from concurrent import futures
from service.contest_service import Contest
from service.submit_service import Submit
from proto import contest_pb2_grpc
from proto import submit_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    contest_pb2_grpc.add_ContestDataServiceServicer_to_server(Contest(), server)
    submit_pb2_grpc.add_SubmitDataServiceServicer_to_server(Submit(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()