#!/usr/bin/env bash
# Copyright (C) dirlt

cp server.conf /usr/local/etc/nginx/servers/upload.conf
sudo nginx -s reload
