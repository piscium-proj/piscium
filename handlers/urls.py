#-*-coding: utf-*-

import tornado.web
from handlers import *

handlers = [
    (r'/', IndexHandler),
    (r'/api/login/account', LoginHandler),
    (r'/api/users', UserListHandler),
    (r'/api/people/(.*)', PeopleHandler),
    #(r'/api/register', RegisterHandler),
    (r'/.*', IndexHandler),
]