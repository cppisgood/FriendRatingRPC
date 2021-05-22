load("@rules_proto_grpc//python:defs.bzl", "python_proto_library")

python_proto_library(
    name = "friend_rating_proto_lib",
    srcs = [
        "proto/contest.proto",
        "proto/submit.proto",
    ],
    visibility = ["//visibility:public"],
)

python_grpc_library(
    name = "friend_rating_proto_grpc_lib",
    protos = ["friend_rating_proto_lib"],
)
