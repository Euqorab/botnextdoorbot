# coding=utf-8

from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
from graia.application.message.chain import MessageChain
import asyncio

from graia.application.message.elements.internal import Plain
from graia.application.friend import Friend
from graia.application.group import Group, Member

from core.message_handler import MsgHandler
from mist import logger as log
from mist import config_util as config

import threading


aqiang_id = 986562745


class Bot:
    send_msg_flag = True

    def start(self):

        handler = MsgHandler()
        # handler.initHandler()

        loop = asyncio.get_event_loop()

        bcc = Broadcast(loop=loop)
        app = GraiaMiraiApplication(
            broadcast=bcc,
            connect_info=Session(
                host="http://localhost:12012",  # 填入 httpapi 服务运行的地址
                authKey=config.Config().get_auth_key(),  # 填入 authKey
                account=config.Config().get_account_id(),  # 你的机器人的 qq 号
                websocket=True  # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
            )
        )

        @bcc.receiver("FriendMessage")
        async def friend_message_listener(app: GraiaMiraiApplication, friend: Friend, message: MessageChain):
            msg = message.asDisplay()
            log.i("receive friend message: %s" % msg)

            should_respond, msg_type, msg = handler.handle(msg, friend=friend)
            log.i("should respond: %s, type: %s, msg %s" % (should_respond, msg_type[1], msg))

            if should_respond:
                result = False
                if msg_type[0] == MsgHandler.TYPE_IMG[0]:
                    result = await app.sendFriendMessage(friend, MessageChain.create([msg]))
                elif msg_type[0] == MsgHandler.TYPE_MSG[0]:
                    result = await app.sendFriendMessage(friend, MessageChain.create([Plain(msg)]))

                log.i("send type: %s, result: %s" % (msg_type[1], result))

        @bcc.receiver("GroupMessage")
        async def group_message_listener(app: GraiaMiraiApplication, group: Group, member: Member, message: MessageChain):
            msg = message.asDisplay()
            log.i("receive group message: %s" % msg)

            should_respond, msg_type, msg = handler.handle(msg)
            log.i("should respond: %s, type: %s, msg %s" % (should_respond, msg_type[1], msg))

            if member.id == aqiang_id:
                should_respond = False

            log.i("send msg flag: %s" % self.send_msg_flag)

            if self.send_msg_flag and should_respond:
                result = await app.sendGroupMessage(group, MessageChain.create([msg]))

                log.i("send type: %s, result: %s" % (msg_type[1], result))
                if result:
                    self.set_send_msg_flag(False)
                    threading.Timer(5.0, self.set_send_msg_flag).start()

        app.launch_blocking()

    def set_send_msg_flag(self, new_flag=True):
        lock = threading.Lock()
        lock.acquire()
        self.send_msg_flag = new_flag
        lock.release()
        log.i("set send msg flag: %s" % new_flag)
