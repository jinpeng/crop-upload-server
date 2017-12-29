#!/usr/bin/env python
# coding=utf-8

import configparser
import falcon
import uptoken

config = configparser.ConfigParser()
config.read('config.ini')
access_key = config['qiniu']['access_key']
secret_key = config['qiniu']['secret_key']
bucket_name = config['qiniu']['bucket_name']

api = application = falcon.API()
uptoken = uptoken.UpToken(access_key, secret_key, bucket_name)
api.add_route('/uptoken', uptoken)
