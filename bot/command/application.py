# coding=utf-8
import os
import subprocess
import time
from win32api import ShellExecute
from mist import logger as log

RES_PATH = os.path.abspath(os.path.dirname(
    os.path.abspath(__file__)) + os.path.sep + ".." + os.path.sep + ".." + os.path.sep + "res"
                           )

ADB_PATH = "Z:\\AirtestIDE_2019-04-16_py3_win64\\AirtestIDE_2019-04-16_py3_win64\\airtest" \
           "\\core\\android\\static\\adb\\windows\\adb"

PYTHON37_PATH = "C:\\Users\\wy\\AppData\\Local\\Programs\\Python\\Python37-32\\python"




def runCmd(cmd):
    print(cmd)
    popen = subprocess.Popen(cmd, shell=False)
    popen.wait()
    # return popen.stdout.readlines()


class Arknights:
    cmd = ["帮我开方舟脚本"]

    def __init__(self):
        self.mumu_path = os.path.join(RES_PATH, "application", "mumu.lnk")
        self.script_path = os.path.join(RES_PATH, "script", "arknights.air", "arknights.py")

    def run(self):
        cmd = "%s %s" % (PYTHON37_PATH, self.script_path)
        log.i(runCmd(cmd))
