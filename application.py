#-*-coding: utf-*-

import os
import tornado.web
from tornado.web import url
from tornado.options import define, options

from handles import IndexHandler

define ('port', default=8000, help='run on the given port', type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/.*', tornado.web.RedirectHandler,{'url':'/'})
        ]

        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), 'templates'),
            static_path = os.path.join(os.path.dirname(__file__), 'static'),
            web_title = '',
            cookie_secrets = "b'B54pC+IfQvi/URHzbEUM+I4qazxvHEXZgXiRN2lWtBk='",
            xsrf_cookies = True,
        )
        tornado.web.Application.__init__(self,handlers, **settings)

application = Application()