# coding=utf-8

import os
from random import randint
from graia.application.message.elements.internal import Image
from mist import logger as log

res_path = os.path.abspath(
    os.path.dirname(os.path.abspath(__file__))
    + os.path.sep + ".." +
    os.path.sep + ".." +
    os.path.sep + "res"
)


class Img(object):
    ext = ['.jpg', ".png", ".gif", ".bmp", ".jpeg"]

    def __init__(self):
        self.path = res_path + "\\img"

    def getRandImg(self):
        if self.path is None:
            return None
        elif os.path.isdir(self.path):
            img_list = []
            for root, dirs, files in os.walk(self.path):
                for file in files:
                    if os.path.splitext(file)[1] in self.ext:
                        img_list.append(file)
            img_path = os.path.join(self.path, img_list[randint(0, len(img_list) - 1)])
            img = Image.fromLocalFile(img_path) if len(img_list) > 0 else None
            return img
        elif os.path.isfile(self.path):
            return self.path
        else:
            return None


class EroImage(Img):
    cmd = [".*[来搞整].*[瑟色涩]图.*"]

    def __init__(self):
        super().__init__()
        self.path = res_path + "\\img\\ero"
