#-*-coding: utf-*-

from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    """Basic handlers classes"""

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

    def set_default_headers(self):
        pass

    def write_error(self, status_code, **kwargs):
        pass

class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('login.html', error="")