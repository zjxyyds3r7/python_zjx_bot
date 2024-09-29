import abc
from math import *

sin(1)


class TextInfo:
    @abc.abstractmethod
    def isReplyPerson(self, NickName: str) -> bool:
        """
        用于指定私聊中这个人是否要回复这类消息(以及帮助文档中是否要显示)
        :param NickName: 用户昵称
        :return: 真假值表示是否回复
        """
        pass

    @abc.abstractmethod
    def isReplyGroup(self, GroupName: str) -> bool:
        """
        用于指定群聊中这个群是否要回复这类消息(以及帮助文档中是否要显示)
        :param GroupName: 群聊名称
        :return: 真假值表示是否回复
        """
        pass

    # @abc.abstractmethod
    # def isPersonReplyText(self, NickName: str, Message: str) -> bool:
    #     """
    #     用于指定私聊中这条消息是否要用此类规则回复
    #     :param NickName: 用户昵称
    #     :param Message: 消息文本
    #     :return: 真假值表示是否回复
    #     """
    #     pass
    #
    # @abc.abstractmethod
    # def isGroupReplyText(self, isAt: bool, GroupName: str, NickName: str, Message: str) -> bool:
    #     """
    #     用于指定群聊中这条消息是否要用此类规则回复
    #     :param isAt: 是否被艾特
    #     :param GroupName: 群聊名称
    #     :param NickName: 发消息人的昵称
    #     :param Message: 消息文本
    #     :return: 真假值表示是否回复
    #     """
    #     pass

    @abc.abstractmethod
    def PersonReplyText(self, NickName: str, Message: str, user) -> str:
        """
        私聊是否回复 如果回复返回回复的内容 如果不回复返回None
        :param user: 传递msg中的user字段方便后续发消息
        :param NickName: 昵称
        :param Message: 消息
        :return: 回复的内容或者None
        """
        pass

    @abc.abstractmethod
    def GroupReplyText(self, isAt: bool, GroupName: str, NickName: str, Message: str, user) -> str:
        """
        群聊消息是否回复 如果回复返回回复的内容 如果不回复返回None
        :param user: 传递msg中的user字段方便后续发消息
        :param isAt: 是否被艾特
        :param GroupName: 群聊名称
        :param NickName: 用户昵称
        :param Message: 消息文本
        :return: 回复的内容或者None
        """
        pass

    @abc.abstractmethod
    def GroupHelp(self) -> str:
        """
        在群聊内显示的帮助文字
        :return: 帮助文字
        """
        pass

    @abc.abstractmethod
    def PersonHelp(self) -> str:
        """
        在私聊内显示的帮助文字
        :return: 帮助文字
        """
        pass


class DefaultInfo(TextInfo):
    def isReplyPerson(self, NickName: str) -> bool:
        return False

    def isReplyGroup(self, GroupName: str) -> bool:
        return False

    def PersonReplyText(self, NickName: str, Message: str) -> str:
        o = Message
        try:
            replaceList = [["（", '('], ['）', ')'], ['–', '-'], [' ', '']]
            for r in replaceList:
                Message = Message.replace(r[0], r[1])
            Message = Message.replace('度', '*pi/180').replace('count', '')
            return f'To {NickName}\n在Python中计算{o}的结果为{eval(Message)}'
        except:
            pass
        return '你好 我是zjxbot 你说的我没有听懂 对我说help获取帮助'

    def GroupReplyText(self, isAt: bool, GroupName: str, NickName: str, Message: str) -> str:
        o = Message
        try:
            replaceList = [["（", '('], ['）', ')'], ['–', '-'], [' ', '']]
            for r in replaceList:
                Message = Message.replace(r[0], r[1])
            Message = Message.replace('度', '*pi/180').replace('count', '')
            return f'To {NickName}\n在Python中计算{o}的结果为{eval(Message)}'
        except:
            pass
        return '你好 我是zjxbot 你说的我没有听懂 对我说help获取帮助'

    def GroupHelp(self) -> str:
        pass

    def PersonHelp(self) -> str:
        pass


class EmptyInfo(TextInfo):
    def isReplyPerson(self, NickName: str) -> bool:
        return False

    def isReplyGroup(self, GroupName: str) -> bool:
        return False

    def PersonReplyText(self, NickName: str, Message: str) -> str:
        return '你好 我是zjxbot 有什么可以帮助你 对我说help获取帮助'

    def GroupReplyText(self, isAt: bool, GroupName: str, NickName: str, Message: str) -> str:
        return '你好 我是zjxbot 有什么可以帮助你 对我说help获取帮助'

    def GroupHelp(self) -> str:
        pass

    def PersonHelp(self) -> str:
        pass
