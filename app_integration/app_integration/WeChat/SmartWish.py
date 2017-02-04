#coding: utf-8
import time, itchat


SINCERE_WISH = u'Best wishes for %s, Happy new year 2017...'
REAL_SINCERE_WISH = u'Best wishes for %s, you are my best and sincere friend...'

def send_wishes():
    friendlist = itchat.get_friends(update=True)[1:]
    for friend in friendlist:
        print(SINCERE_WISH % (friend['UserName'] or friend['NickName']), friend['UserName'])
        time.sleep(.5)

def send_special_wishes(chatroomName='wishgroup'):
    itchat.get_chatrooms(update=True)
    chatrooms = itchat.search_chatrooms(name=chatroomName)
    if chatroomName is None:
        print(u'search result is none')
    else:
        chatroom = itchat.update_chatroom(chatroom[0]['UserName'])
        for friend in chatroom['MemberList']:
            friend = itchat.search_friends(userName=friend['UserName'])
            print(REAL_SINCERE_WISH % (friend['DisplayName'] or friend['NickName']), friend['UserName'])
            time.sleep(.5)

itchat.auto_login(True)

send_wishes()
send_special_wishes()