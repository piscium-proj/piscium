# -*-coding: utf-*-

import tornado.web
from tornado.options import define, options
from handlers.urls import handlers
import config
from utils.db import mariadb_connection
from utils.imdb import redis_connection

define('port', default=8000, help='run on the given port', type=int)


class Application(tornado.web.Application):
    '''main web aplication engine'''

    def __init__(self):
        tornado.web.Application.__init__(self, handlers, **config.settings)
        self.db = mariadb_connection
        self.redis = redis_connection
        options.log_file_prefix = config.log_file
        options.logging = config.log_level


application = Application()
