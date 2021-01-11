# coding=utf-8

import yaml
import os


class Config:
    path = os.path.abspath(
        os.path.dirname(os.path.abspath(__file__))
        + os.path.sep + ".." +
        os.path.sep + ".." +
        os.path.sep + ".." +
        os.path.sep + "config"
    )

    def get_account_id(self):
        file = open(os.path.join(self.path, "Console/AutoLogin.yml"), encoding='UTF-8')
        account = yaml.load(file, Loader=yaml.FullLoader)
        return account["accounts"][1]["account"]

    def get_auth_key(self):
        print(self.path)
        file = open(os.path.join(self.path, "net.mamoe.mirai-api-http/setting.yml"), encoding='UTF-8')
        setting = yaml.load(file, Loader=yaml.FullLoader)
        return setting["authKey"]


if __name__ == "__main__":
    print(Config().get_account_id())
