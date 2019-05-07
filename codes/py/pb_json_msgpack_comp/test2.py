#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import time

import json

import msgpack

from test2_pb2 import BatchHelloRequest, HelloRequest


def pb_bench(n):
    breq = BatchHelloRequest()
    for i in range(100):
        req = HelloRequest()
        req.title = 'hello'
        req.name = 'world'
        req.version = 3;
        req.tags.extend([1, 2, 3, 4])
        req.desc = 'nenaxxx'
        req.f0 = 'abcdefg'
        req.f1 = 'hijklmn'
        req.f2 = 'opqrst'
        breq.items.extend([req])

    start = time.time()
    for i in range(n):
        data = breq.SerializeToString()
    stop = time.time()
    print('pb save = {:.2f}. size = {}'.format(stop - start, len(data)))

    start = time.time()
    for i in range(n):
        breq.ParseFromString(data)
    stop = time.time()
    print('pb load = {:.2f}'.format(stop - start))


def json_bench(n):
    js = []
    for i in range(100):
        x = dict(
            title='hello',
            name='world',
            version=3,
            tags=[1, 2, 3, 4],
            desc='nenaxxx',
            f0='abcdefg',
            f1='hijklmn',
            f2='opqrst'
        )
        js.append(x)

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


def msgpack_bench(n):
    js = []
    for i in range(100):
        x = dict(
            title='hello',
            name='world',
            version=3,
            tags=[1, 2, 3, 4],
            desc='nenaxxx',
            f0='abcdefg',
            f1='hijklmn',
            f2='opqrst'
        )
        js.append(x)

    start = time.time()
    for i in range(n):
        data = msgpack.packb(js)
    stop = time.time()
    print('msgpack save = {:.2f}. size = {}'.format(stop - start, len(data)))

    start = time.time()
    for i in range(n):
        js = msgpack.unpackb(data)
    stop = time.time()
    print('msgpack load = {:.2f}'.format(stop - start))


n = 10000
pb_bench(n)
json_bench(n)
msgpack_bench(n)
