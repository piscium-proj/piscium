#-*-coding: utf-*-

import tornado.web
from tornado.options import define, options
from handlers.urls import handlers
from config import settings

define ('port', default=8000, help='run on the given port', type=int)

class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, handlers, **settings)

application = Application()