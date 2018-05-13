#-*-coding: utf-*-

import uuid
import logging
import json
from constants import SESSION_EXPIRES_SECONDS

class Session(object):
    """"""
    def __init__(self, request_handler):
        self.request_handler = request_handler
        session_id = self.request_handler.get_secure_cookie("session_id")
        if not session_id:
            # User logins by first time
            # Set a session_id, globally unique
            self.session_id = uuid.uuid4().hex
            self.data = {}
        else:
            # Read data from redis by session_id
            try:
                data = self.redis.get("sess_%s" % session_id)
            except Exception as error:
                logging.error(error)
                self.data = {}
            if not data:
                self.data = {}
            else:
                self.data = json.loads(data)

def save(self):
    json_data = json.dumps(self.data)
    try:
        self.redis.setex("sess_%s" % self.session_id, SESSION_EXPIRES_SECONDS, json_data)
    except Exception as error:
        logging.error(error)
        raise Exception("save session failed")
    else:
        self.request_handler.set_secure_cookie("session_id", self.session_id)

def clear(self):
    self.request_handler.clear_cookie("session_id")
    try:
        self.redis.delete("sess %s" % self.session_id)
    except Exception as error:
        logging.error(error)

#session = Session(request_handler = self)
#session.session_id = 'xyz357'

# First time login or exception {}
#session.data = {}
#session.data["user_id"] = 123
#session.data["user_name"] = 'abc'
# redis
#session.save()
# {"user_id":123, "user_name":"abc"}
# RequestHandler.get_secure_cookie()
# set_secure_cookie
