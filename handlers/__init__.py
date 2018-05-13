#-*-coding: utf-*-

from tornado.web import RequestHandler
from handlers.session import Session
import logging

class BaseHandler(RequestHandler):
    """Basic handlers classes"""

    @property
    def db(self):
        return  self.application.db

    def get_current_user(self):
        return self.get_secure_cookie("user")

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

class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('index.html', error="")
        #logging.debug("debug msg")

class LoginHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render('login.html', error="")
        # logging.debug("debug msg")

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        # The authenticate method should match  a username and password
        # to a username and password hash in the database users table.
        # Waiting for complete this part
        auth = self.db.authenticate(username, password)

        def set_current_user(self, user):
            if user:
                self.set_secure_cookie("user", tornado.escape.json_encode(user))

        if auth:
            self.set_current_user(username)
            self.redirect(self.get_argument("next", u"/"))
        else:
            error_msg = u"?error=" + tornado.escape.url_escape("Login incorrect")
            self.redirect(u"/login") + error_msg
