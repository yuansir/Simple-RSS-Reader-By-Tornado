# -*- coding: utf-8 -*-
from handlers import RequestHandler
import feedparser


class IndexHandler(RequestHandler):
    def get(self):
        self.render('index.html')

