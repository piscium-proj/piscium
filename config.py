#-*-coding: utf-*-

import os

#web
settings = dict(
    web_title = 'Piscium',
    template_path = os.path.join(os.path.dirname(__file__), 'template'),
    static_path = os.path.join(os.path.dirname(__file__), 'static'),
    cookie_secret = "b'B54pC+IfQvi/URHzbEUM+I4qazxvHEXZgXiRN2lWtBk='",
    xsrf_cookies = True,
    debug = True,
)

#mariadb
mariadb_option = dict(
    host='127.0.0.1',
    user='root',
    password='511',
    database='piscium'
)

#redis
redis_option = dict(
    host='127.0.0.1',
    port='6379'
)

#log
log_file = os.path.join(os.path.dirname(__file__), "logs/log")
log_level = "debug"