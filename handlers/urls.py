#-*-coding: utf-*-

import tornado.web
from handlers import *

handlers = [
    (r'/', IndexHandler),
    (r'/.*', tornado.web.RedirectHandler,{'url':'/'})
]