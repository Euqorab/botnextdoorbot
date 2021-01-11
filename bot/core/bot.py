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


aqiang_id = 123456


class Bot:
    send_msg_flag = True

    def start(self):

        message_handler = MsgHandler()
        # message_handler.initHandler()

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
        async def friend_message_listener(graia_app: GraiaMiraiApplication, friend: Friend, message: MessageChain):

            async def friend_sender(send_msg):
                result = await graia_app.sendFriendMessage(friend, MessageChain.create([send_msg]))
                if result:
                    self.set_send_msg_flag(False)
                    threading.Timer(5.0, self.set_send_msg_flag).start()

            msg = message.asDisplay()
            log.i("receive friend message: %s" % msg)
            await message_handler.handle(msg, friend_sender, friend=friend)

        @bcc.receiver("GroupMessage")
        async def group_message_listener(graia_app: GraiaMiraiApplication, group: Group, member: Member, message: MessageChain):

            async def group_sender(send_msg):
                should_respond = True
                if member.id == aqiang_id:
                    should_respond = False

                if should_respond:
                    result = await graia_app.sendGroupMessage(group, MessageChain.create([send_msg]))
                    if result:
                        self.set_send_msg_flag(False)
                        threading.Timer(5.0, self.set_send_msg_flag).start()

            msg = message.asDisplay()
            log.i("receive group message: %s" % msg)
            await message_handler.handle(msg, group_sender)

        app.launch_blocking()

    def set_send_msg_flag(self, new_flag=True):
        lock = threading.Lock()
        lock.acquire()
        self.send_msg_flag = new_flag
        lock.release()
        log.i("set send msg flag: %s" % new_flag)
