# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import urls
import modules
import settings
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

define("port", default=settings.PORT, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        settings.SETTING['ui_modules'] = modules.ui_modules
        tornado.web.Application.__init__(self, urls.handler, **settings.SETTING)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
