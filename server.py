#-*-coding: utf-*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.autoreload
from application import application

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(tornado.options.options.port)
    loop = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(loop)
    loop.start()