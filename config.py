#-*-coding: utf-*-

import os

settings = dict(
    web_title = '',
    template_path = os.path.join(os.path.dirname(__file__), 'templates'),
    static_path = os.path.join(os.path.dirname(__file__), 'view'),
    cookie_secret = "b'B54pC+IfQvi/URHzbEUM+I4qazxvHEXZgXiRN2lWtBk='",
    xsrf_cookies = True,
    debug = True,
)