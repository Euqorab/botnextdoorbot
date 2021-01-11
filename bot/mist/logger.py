# coding=utf-8

import mist.time_util as tu


def i(*msg):
    print("[%s][INFO] %s" % (tu.get_time_str(), msg))


def m(*msg):
    print("[%s][MSG] %s" % (tu.get_time_str(), msg))


def e(*msg):
    print("[%s][ERROR] %s" % (tu.get_time_str(), msg))
