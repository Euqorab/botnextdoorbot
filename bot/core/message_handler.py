# coding=utf-8

from graia.application.message.elements.internal import Plain

from mist import logger as log
from command.img import EroImage
from command.application import Arknights

import re


class MsgHandler:
    def __init__(self):
        # todo: init corpus file
        return

    async def handle(self, msg: str, sender, friend=None, group=None, member=None):
        if friend is not None and friend.id == 361307103:
            for cmd in Arknights.cmd:
                if re.search(cmd, msg):
                    await Arknights().run(sender)

        for cmd in EroImage.cmd:
            if re.search(cmd, msg):
                img = EroImage().get_rand_img()
                log.i("img: %s" % img)
                await sender(img)
