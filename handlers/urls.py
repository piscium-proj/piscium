#-*-coding: utf-*-

import tornado.web
from handlers import *

handlers = [
    (r'/', IndexHandler),
    (r'/api/login/account', LoginHandler),
    (r'/.*', tornado.web.RedirectHandler,{'url':'/'})
]