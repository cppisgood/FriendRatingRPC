# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging

import grpc

from proto import submit_pb2
from proto import submit_pb2_grpc
from proto import contest_pb2
from proto import contest_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = contest_pb2_grpc.ContestDataServiceStub(channel)
        response = stub.GetContestData(contest_pb2.ContestDataRequest(
            platform = 'nowcoder',
            handle = '861349648'
        ))
    print(response)
# def run():
#     # NOTE(gRPC Python Team): .close() is possible on a channel and should be
#     # used in circumstances in which the with statement does not fit the needs
#     # of the code.
#     with grpc.insecure_channel('localhost:50051') as channel:
#         stub = submit_pb2_grpc.SubmitDataServiceStub(channel)
#         response = stub.GetSubmitData(submit_pb2.SubmitDataRequest(
#             platform = 'luogu',
#             handle = 'Zmm2019'
#         ))
#     print(response)


if __name__ == '__main__':
    logging.basicConfig()
    run()
