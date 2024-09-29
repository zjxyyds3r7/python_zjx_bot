from Info_class import TextInfo


class DirtyWordDel(TextInfo):
    groups = ['开局一条狗', 'Java技术交流群']

    def isReplyPerson(self, NickName: str) -> bool:
        return True

    def isReplyGroup(self, GroupName: str) -> bool:
        if GroupName in self.groups:
            return True
        return False

    def PersonReplyText(self, NickName: str, Message: str, user) -> str:
        if 'sb' in Message.lower() or '傻逼' in Message:
            return f'{NickName}不许骂人'
        return None

    def GroupReplyText(self, isAt: bool, GroupName: str, NickName: str, Message: str, user) -> str:
        if 'sb' in Message.lower() or '傻逼' in Message:
            return ' ' + f'{NickName} 不许骂人'
        return None

    def GroupHelp(self) -> str:
        return '如果在群里发送sb,傻逼会被提示'

    def PersonHelp(self) -> str:
        return '如果和我说sb,傻逼会被提示'
