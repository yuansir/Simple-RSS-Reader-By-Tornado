# -*- coding: utf-8 -*-
from tornado.web import UIModule as BaseUIModule
import pymongo
import settings

class UIModule(BaseUIModule):
    db = pymongo.Connection(settings.DB['mongo']['host'], settings.DB['mongo']['port']).rss;
