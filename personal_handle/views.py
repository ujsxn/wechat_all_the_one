# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib

from rest_framework.views import APIView
from rest_framework.response import Response


class DefaultView(APIView):

    def get(self, request):

        signature = request.query_params.get("signature", None)
        timestamp = request.query_params.get("timestamp", None)
        nonce = request.query_params.get("nonce", None)
        echostr = request.query_params.get("echostr", None)

        if all([signature, timestamp, nonce, echostr]):

            raw_list = ["token", timestamp, nonce]
            raw_list.sort()

            # 将三个参数字符串拼接成一个字符串进行sha1加密
            sha = hashlib.sha1()
            sha.update("".join(raw_list))

            # 开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
            if signature == sha.hexdigest():
                return Response(echostr)
            else:
                return Response("check error")

        else:

            return Response("no arg")
