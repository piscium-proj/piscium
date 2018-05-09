#-*-coding: utf-*-

import tornado.web
from handlers import IndexHandler

handlers = [
    (r'/', IndexHandler),
    (r'/.*', tornado.web.RedirectHandler,{'url':'/'})
]