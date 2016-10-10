#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re
import urllib
import socket
import time
import smtplib
from email.mime.text import MIMEText

#############
#To address
mailto_list=["jesuie@126.com"]
#####################
#Set server, account, password and email postfix


# no tls
mail_host="smtp.126.com"
mail_user="jesuie"
mail_pass=""
mail_postfix="126.com"

'''
#tls
mail_host="smtp-mail.outlook.com:587"
mail_user="xx@hotmail.com"
mail_pass="xx"
mail_postfix="hotmail.com"
'''

'''
#tls
mail_host="smtp.gmail.com:587"
mail_user="xx@gmail.com"
mail_pass="xx"
mail_postfix="gmail.com"
'''
######################


def send_mail(to_list,sub,content):
	'''
	to_list: to address
	sub:subject
	content:content
	send_mail("aaa@126.com","sub","content")
	'''
	me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
	msg = MIMEText(content)
	msg['Subject'] = sub
	msg['From'] = me
	msg['To'] = ";".join(to_list)
	try:
		s = smtplib.SMTP()
		s.connect(mail_host)
		s.starttls() # TLS need this
		s.login(mail_user,mail_pass)
		s.sendmail(me, to_list, msg.as_string())
		s.close()
		return True
	except Exception as e:
		print (e)
		return False


'''
def getip():
	sock = socket.create_connection(('ns1.dnspod.net', 6666))
	ip = sock.recv(16)
	sock.close()
	return ip
'''

def getip():
	f = urllib.urlopen("http://www.canyouseeme.org/")
	html_doc = f.read()
	f.close()
	print (html_doc)
	m = re.search('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',html_doc)
	print (m.group(0))
	data=m.group()
	return data

if __name__ == '__main__':
	current_ip = None

	while True:
		try:
			ip = getip()
			print (ip)
			if current_ip != ip:
				# subject maybe has senstive words smtp server will return "SPM" error code
				if send_mail(mailto_list,"Raspberry Pi", 'Raspberry Pi External IP Addreds is ' + ip + ' ...!'):
					urrent_ip = ip
					#print('Send OK')
		except Exception as e:
			print (e)
			pass
		time.sleep(60) # Check the ip address every one minute