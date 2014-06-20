# -*- coding: utf-8 -*-
from tornado.web import RequestHandler as BaseRequestHandler
import json
import pymongo
import settings


class RequestHandler(BaseRequestHandler):
    db = pymongo.Connection(settings.DB['mongo']['host'], settings.DB['mongo']['port']).rss;

    def response_json(self, status=1, msg='', *data):
        ret = {
            "status": status,
            "msg": msg,
            "data": data
        }
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(json.dumps(ret, default=str, encoding="utf-8", ensure_ascii=False))