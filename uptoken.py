#!/usr/bin/env python
# coding=utf-8

import falcon
from qiniu import Auth

class UpToken(object):
    def __init__(self, access_key, secret_key, bucket_name):
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name

    def on_get(self, req, resp):
        key = ''
        q = Auth(self.access_key, self.secret_key)
        policy = {
            # 'callbackUrl':'https://requestb.in/1c7q2d31',
            # 'callbackBody':'filename=$(fname)&filesize=$(fsize)'
            # 'persistentOps':'imageView2/1/w/200/h/200'
        }
        token = q.upload_token(self.bucket_name, key, 3600, policy)
        print(token)
        resp.append_header("Access-Control-Allow-Origin", "*")
        resp.body = '{"token": "' + token + '"}'
        resp.status = falcon.HTTP_200

