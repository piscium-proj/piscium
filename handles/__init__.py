#-*-coding: utf-*-

from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    def get_current_user(self):
        user_id = self.get_secure_cookie('uid')
        if not user_id:
            return None
        return json_decode(user_id)

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html', error="")