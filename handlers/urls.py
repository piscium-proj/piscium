#-*-coding: utf-*-

import tornado.web
from handlers import *

handlers = [
    (r'/', IndexHandler),
    (r'/login/', LoginHandler),
    (r'/.*', tornado.web.RedirectHandler,{'url':'/'})
]