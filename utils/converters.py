import datetime

def datetime2string(dt):
    if isinstance(dt, datetime.datetime):
        return dt.__str__()