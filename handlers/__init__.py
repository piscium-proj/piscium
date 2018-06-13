#-*-coding: utf-*-

from tornado.web import RequestHandler
import tornado.escape
import json
from utils.converters import datetime2string
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

    def post(self, *args, **kwargs):
        cursor = self.db.cursor()
        request_data = json.loads(self.request.body)
        username = request_data['userName']
        cursor.execute("SELECT * FROM users_profile WHERE username=%s", (username))
        userdata = cursor.fetchone()
        if userdata:
            userid = userdata[0]
            userpwd = userdata[3]
            if request_data['password'] == userpwd:
                cursor.execute("SELECT user_authorityid FROM users WHERE userid=%s", (userid))
                user_authorityid = cursor.fetchone()[0]
                cursor.execute("SELECT authorityname FROM authorities WHERE authorityid=%s", (user_authorityid))
                user_authority = cursor.fetchone()[0]
                self.db.commit()
                avatar = userdata[5]
                notifycount = 0
                response_data = {
                    'status': 'ok',
                    'type': 'account',
                    'currentAuthority': user_authority,
                    'userid': userid,
                    'username': username,
                    'avatar': avatar,
                    'notifycount': notifycount,
                }
            else:
                response_data = {
                    'status': 'error',
                    'type': 'account',
                    'currentAuthority': 'guest'
                }
        else:
            response_data = {
                'status': 'error',
                'type': 'account',
                'currentAuthority': 'guest'
            }
        response_json_data = json.dumps(response_data)
        print(response_json_data)
        self.write(response_json_data)

class UserListHandler(BaseHandler):

    def get(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        response_list = []
        try:
            for user in users:
                cursor.execute("SELECT * FROM users_profile WHERE userid=%s", (user[0]))
                userprofile = cursor.fetchone()
                cursor.execute("SELECT * FROM authorities WHERE authorityid=%s", (user[1]))
                userauthority = cursor.fetchone()
                cursor.execute("SELECT * FROM statuses WHERE statusid=%s", (user[2]))
                userstatus = cursor.fetchone()
                cursor.execute("SELECT * FROM users_role WHERE userid=%s", (user[0]))
                userrole = cursor.fetchone()
                cursor.execute("SELECT * FROM roles WHERE roleid=%s", (userrole[1]))
                userroledesc = cursor.fetchone()
                response_data = {
                    'id': str(userprofile[0]),
                    'username': userprofile[1],
                    'href': 'https://localhost:8000/people/' + str(user[0]),
                    'email': userprofile[2],
                    'logo': userprofile[5],
                    'createdAt': userprofile[7],
                    'updatedAt': userprofile[8],
                    'role': userauthority[1],
                    'status': userstatus[1],
                    'position': userroledesc[2],
                }
                response_list.append(response_data)
            response_json_data = json.dumps(response_list, default=datetime2string)
            print(response_json_data)
            self.write(response_json_data)
        except Exception as e:
            raise e

class PeopleHandler(BaseHandler):

    def get(self, userid):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT * FROM users_profile WHERE userid=%s", userid)
            userprofile = cursor.fetchone()
            cursor.execute("SELECT * FROM users_role WHERE userid=%s", userid)
            userrole = cursor.fetchone()
            cursor.execute("SELECT * FROM roles WHERE roleid=%s", userrole[1])
            userroledesc = cursor.fetchone()
            notifycount = 0
            response_data = {
                'userid': str(userprofile[0]),
                'name': userprofile[1],
                'avatar': userprofile[5],
                'notifyCount': str(notifycount),
                'position': userroledesc[2],
            }
            response_json_data = json.dumps(response_data)
            print (response_json_data)
            self.write(response_json_data)
        except Exception as e:
            raise e

    # def post(self):
    #     username = self.get_argument("username", "")
    #     password = self.get_argument("password", "")
    #     # The authenticate method should match  a username and password
    #     # to a username and password hash in the database users table.
    #     # Waiting for complete this part
    #     auth = self.db.authenticate(username, password)
    #
    #     def set_current_user(self, user):
    #         if user:
    #             self.set_secure_cookie("user", tornado.escape.json_encode(user))
    #
    #     if auth:
    #         self.set_current_user(username)
    #         self.redirect(self.get_argument("next", u"/"))
    #     else:
    #         error_msg = u"?error=" + tornado.escape.url_escape("Login incorrect")
    #         self.redirect(u"/login") + error_msg

class RegisterHandler(BaseHandler):

    def post(self, *args, **kwargs):
        request_data = json.loads(self.request.body)
        print (request_data)