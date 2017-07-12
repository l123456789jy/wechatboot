# coding=utf8
import itchat
from tuling import get_response

@itchat.msg_register('Text')
def text_reply(msg):
    if u'作者' in msg['Text'] or u'主人' in msg['Text']:
        return u'Lazy'
    elif u'源代码' in msg['Text'] or u'获取文件' in msg['Text']:
        itchat.send('@fil@main.py', msg['FromUserName'])
        return u'还没开发呢'
    elif u'获取图片' in msg['Text']:
        itchat.send('@img@applaud.gif', msg['FromUserName'])  # there should be a picture
    else:
        return get_response(msg['Text']) or u'' + msg['Text']


@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def atta_reply(msg):
    return ({'Picture': u'图片', 'Recording': u'录音',
             'Attachment': u'附件', 'Video': u'视频', }.get(msg['Type']) +
            u'已下载到本地')  # download function is: msg['Text'](msg['FileName'])


@itchat.msg_register(['Map', 'Card', 'Note', 'Sharing'])
def mm_reply(msg):
    if msg['Type'] == 'Map':
        return u'收到位置分享'
    elif msg['Type'] == 'Sharing':
        return u'收到分享' + msg['Text']
    elif msg['Type'] == 'Note':
        return u'收到：' + msg['Text']
    elif msg['Type'] == 'Card':
        return u'收到好友信息：' + msg['Text']['Alias']


@itchat.msg_register('Text', isGroupChat=True)
def group_reply(msg):
    if msg['isAt']:
        return u'@%s\u2005%s' % (msg['ActualNickName'],
                                 get_response(msg['Text']) or u'收到：' + msg['Text'])


@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg(u'我是小L,欢迎撩我！', msg['RecommendInfo']['UserName'])


itchat.auto_login()
itchat.run()
