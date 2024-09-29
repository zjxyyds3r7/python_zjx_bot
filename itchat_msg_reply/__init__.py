import itchat
from itchat.content import TEXT, NOTE
from Settings import *
from Info_class import EmptyInfo, DefaultInfo


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply_group(msg):
    is_at = msg.isAt
    group_name = msg.User['NickName']
    nick_name = msg.actualNickName
    message = msg.text.split(" ")[-1]
    if not message and is_at:
        return EmptyInfo().GroupReplyText(is_at, group_name, nick_name, message)
    if is_at and message in help_list:
        return '\n'.join([
            t.GroupHelp() for t in TextInfoList
            if t.isReplyGroup(group_name)
        ])
    for t in TextInfoList:
        r = t.GroupReplyText(is_at, group_name, nick_name, message, msg.user)
        if t.isReplyGroup(group_name) and r:
            return r
    if is_at:
        return DefaultInfo().GroupReplyText(is_at, group_name, nick_name, message)


@itchat.msg_register(TEXT, isGroupChat=False)
def text_reply_person(msg):
    nick_name = msg.user.RemarkName
    message = msg.text
    if not message:
        return EmptyInfo().PersonReplyText(nick_name, message)
    if message in help_list:
        return '\n'.join([
            t.PersonHelp() for t in TextInfoList
            if t.isReplyPerson(nick_name)
        ])
    for t in TextInfoList:
        r = t.PersonReplyText(nick_name, message, msg.user)
        if t.isReplyPerson(nick_name) and r:
            return r
    return DefaultInfo().PersonReplyText(nick_name, message)


# @itchat.msg_register(NOTE, isGroupChat=True)
# def fun(msg):
#     if '拍了拍' in msg.text:
#         return f'别拍我'

def Send_course_schedule():
    pass


def run():
    itchat.auto_login(hotReload=True)
    itchat.run(True)
