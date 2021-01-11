# coding=utf-8

import time


def get_time_str() -> str:
    now = int(round(time.time() * 1000))
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now / 1000))
