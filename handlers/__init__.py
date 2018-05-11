#-*-coding: utf-*-

from tornado.web import RequestHandler
import logging

class BaseHandler(RequestHandler):
    """Basic handlers classes"""

    @property
    def db(self):
        return  self.application.db

    def get_current_user(self):
        user_id = self.get_secure_cookie('uid')
        if not user_id:
            return None
        return json_decode(user_id)

    def initialize(self):
        pass

    def on_finish(self):
        pass

    def prepare(self):
        pass

    @property
    def redis(self):
        return self.application.redis

    def set_default_headers(self):
        pass

    def write_errenderror(self, status_code, **kwargs):
        pass

class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('index.html', error="")
        #logging.debug("debug msg")