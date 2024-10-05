"""
Datetime features
"""
from datetime import timedelta as delta
import re
import arrow
date_regex = re.compile("^(\d{4})(\d{2})(\d{2})$", flags=re.M)

TIME_FORMAT = "YYYYMMDDHHmmss"
HOUR = 60 * 60
DAY = HOUR * 24
MONTH = DAY * 31


def t2i(t: int):
    return int(arrow.get(t).format(TIME_FORMAT))