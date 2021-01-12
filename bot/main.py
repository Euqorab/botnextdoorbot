# coding=utf-8

from core.bot import Bot
from win32api import ShellExecute
import os


if __name__ == "__main__":
    mcl_path = os.path.abspath(
        os.path.dirname(os.path.abspath(__file__))
        + os.path.sep + ".." +
        os.path.sep + ".." +
        os.path.sep + "mcl.cmd"
    )
    ShellExecute(0, "open", mcl_path, "", "", 1)

    Bot().start()
