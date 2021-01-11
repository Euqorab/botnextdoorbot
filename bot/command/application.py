# coding=utf-8
import os
import subprocess
import threading
from mist import logger as log
from graia.application.message.elements.internal import Plain

RES_PATH = os.path.abspath(os.path.dirname(
    os.path.abspath(__file__)) + os.path.sep + ".." + os.path.sep + ".." + os.path.sep + "res"
                           )

ADB_PATH = "Z:\\AirtestIDE_2019-04-16_py3_win64\\AirtestIDE_2019-04-16_py3_win64\\airtest" \
           "\\core\\android\\static\\adb\\windows\\adb"

PYTHON37_PATH = "C:\\Users\\wy\\AppData\\Local\\Programs\\Python\\Python37-32\\python"

SIMULATOR_RUNNING = False


def runCmd(cmd, should_await=False):
    print(cmd)
    popen = subprocess.Popen(cmd, shell=False)
    if should_await:
        popen.wait()


class RunArknightsThread(threading.Thread):
    def __init__(self, cmd):
        super().__init__()
        self.cmd = cmd

    def run(self) -> None:
        global SIMULATOR_RUNNING
        SIMULATOR_RUNNING = True
        runCmd(self.cmd, should_await=True)
        SIMULATOR_RUNNING = False


class Arknights:
    cmd = ["帮我开方舟脚本"]

    def __init__(self):
        self.mumu_path = os.path.join(RES_PATH, "application", "mumu.lnk")
        self.script_path = os.path.join(RES_PATH, "script", "arknights.air", "arknights.py")

    async def run(self, sender):
        global SIMULATOR_RUNNING

        if not SIMULATOR_RUNNING:
            await sender(Plain("在跑了在跑了"))
            cmd = "%s %s" % (PYTHON37_PATH, self.script_path)
            RunArknightsThread(cmd).start()
        else:
            await sender(Plain("有人在跑着"))
