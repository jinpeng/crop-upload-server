#!/usr/bin/env python
# coding=utf-8

import falcon
import uptoken

access_key = 'NUbGljTaPJ42x7Py1_s7MY2kVrAvgpHnTICdl5_p'
secret_key = 'zhwRBRcvhVWsjwyO3QK_J1U60QMj5TjO_KPzdNXD'
bucket_name = 'jitu'

api = application = falcon.API()
uptoken = uptoken.UpToken(access_key, secret_key, bucket_name)
api.add_route('/uptoken', uptoken)

