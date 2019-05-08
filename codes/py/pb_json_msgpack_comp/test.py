#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import time

import json

import msgpack

from test_pb2 import HelloRequest

from google.protobuf.internal import api_implementation
print('python protobuf API impl = {}'.format(api_implementation.Type()))

import bson

def pb_bench(n):
    req = HelloRequest()
    keys = []
    pids = []
    for i in range(200):
        keys.append("key#%d" % i)
        pids.append(i + 200000)
    req.keys.extend(keys)
    req.pids.extend(pids)

    start = time.time()
    for i in range(n):
        data = req.SerializeToString()
    stop = time.time()
    print('pb save = {:.2f}. size = {}'.format(stop - start, len(data)))

    start = time.time()
    for i in range(n):
        req.ParseFromString(data)
    stop = time.time()
    print('pb load = {:.2f}'.format(stop - start))


def json_bench(n):
    keys = []
    pids = []
    for i in range(200):
        keys.append("key#%d" % i)
        pids.append(i + 200000)
    js = dict(keys = keys, pids = pids)

    start = time.time()
    for i in range(n):
        data = json.dumps(js)
    stop = time.time()
    print('json save = {:.2f}. size = {}'.format(stop - start, len(data)))

    start = time.time()
    for i in range(n):
        js = json.loads(data)
    stop = time.time()
    print('json load = {:.2f}'.format(stop - start))

def bson_bench(n):
    keys = []
    pids = []
    for i in range(200):
        keys.append("key#%d" % i)
        pids.append(i + 200000)
    js = dict(keys = keys, pids = pids)

    start = time.time()
    for i in range(n):
        data = bson.BSON.encode(js)
    stop = time.time()
    print('bson save = {:.2f}. size = {}'.format(stop - start, len(data)))

    start = time.time()
    for i in range(n):
        js = bson.BSON.decode(data)
    stop = time.time()
    print('bson load = {:.2f}'.format(stop - start))

def msgpack_bench(n):
    keys = []
    pids = []
    for i in range(200):
        keys.append("key#%d" % i)
        pids.append(i + 200000)
    js = dict(keys = keys, pids = pids)

    start = time.time()
    for i in range(n):
        data = msgpack.packb(js)
    stop = time.time()
    print('msgpack save = {:.2f}. size = {}'.format(stop - start, len(data)))

    start = time.time()
    for i in range(n):
        js = msgpack.unpackb(data, raw = False)
    stop = time.time()
    print('msgpack load = {:.2f}'.format(stop - start))


n = 100000
json_bench(n)
# save too fucking slow.
# bson_bench(n)
msgpack_bench(n)
pb_bench(n)
