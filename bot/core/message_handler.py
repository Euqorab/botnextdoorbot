# coding=utf-8

from graia.application.message.elements.internal import Plain

from mist import logger as log
from command.img import EroImage
from command.application import Arknights

import re


class MsgHandler:
    TYPE_NONE = [0, "none"]
    TYPE_MSG = [1, "msg"]
    TYPE_IMG = [2, "img"]

    def __init__(self):
        # todo: init corpus file
        return

    def handle(self, msg: str, friend=None, group=None, member=None):
        if friend is not None and friend.id == 773533040:
            for cmd in Arknights.cmd:
                if re.search(cmd, msg):
                    Arknights().run()

        for cmd in EroImage.cmd:
            if re.search(cmd, msg):
                img = EroImage().getRandImg()
                log.i("img: %s" % img)
                return img is not None, self.TYPE_IMG, img

        return False, self.TYPE_NONE, Plain(msg)
