# coding=utf-8


class MsgCache:
    msg_cache = []
    cache_size = 0

    def __init__(self, cache_size):
        self.cache_size = cache_size

    def append(self, msg_tup):
        self.msg_cache.insert(0, msg_tup)
        if self.msg_cache > self.cache_size:
            del self.msg_cache[self.cache_size:]

    def find(self, msg, user_id=None):
        for index, msg_tup in enumerate(self.msg_cache):
            if user_id is not None:
                if msg_tup[0] == msg:
                    return index
            elif user_id == msg_tup[1] and msg == msg_tup[0]:
                return index

