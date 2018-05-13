#-*-coding: utf-*-

from tornado.web import RequestHandler
from handlers.session import Session
import logging

class BaseHandler(RequestHandler):
    """Basic handlers classes"""    """Basic handlers classes"""

    @property
    def db(self):
        return  self.application.db

    def get_current_user(self):
        self.session = Session(self)
        return self.session.data

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

    def write_error(self, status_code, **kwargs):
        pass


    @property
    def db(self):
        return  self.application.db

    def get_current_user(self):
        self.session = Session(self)
        return self.session.data

    def initialize(self):
        pass

    def on_finish(self):
        pass

    def prepare(self):
        self.xsrf_token
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None

    @property
    def redis(self):
        return self.application.redis

    def set_default_headers(self):
        pass

    def write_error(self, status_code, **kwargs):
        pass

class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('index.html', error="")
        #logging.debug("debug msg")