from Settings import *
from random_number import RandomNumber
from dirty_word_del import DirtyWordDel
from itchat_msg_reply import run

TextInfoList.append(RandomNumber())
TextInfoList.append(DirtyWordDel())

if __name__ == '__main__':
    run()
