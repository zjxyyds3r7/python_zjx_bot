import random

from Info_class import TextInfo


class RandomNumber(TextInfo):
    start_list = ['4', '随机数', '取随机数']

    def isReplyPerson(self, NickName: str):
        return True

    def isReplyGroup(self, GroupName: str):
        return True

    def PersonReplyText(self, NickName: str, Message: str, user):
        for s in self.start_list:
            if Message.lower() == s:
                return f'你好，{NickName}，你获得的随机数是: {random.randint(1, 100)}'
        return None

    def GroupReplyText(self, isAt: bool, GroupName: str, NickName: str, Message: str, user):
        if not isAt:
            return None
        for s in self.start_list:
            if Message.lower() == s:
                return f'你好，{NickName}，你获得的随机数是: {random.randint(1, 100)}'

    def GroupHelp(self):
        word = '"' + '"或"'.join(self.start_list) + '"'
        return f'艾特我并输入{word}获取随机数'

    def PersonHelp(self):
        word = '"' + '"或"'.join(self.start_list) + '"'
        return f'对我说{word}获取随机数'
