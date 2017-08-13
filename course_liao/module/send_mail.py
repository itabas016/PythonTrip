#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import sys

PORT = 25
PORT_SSL = 587


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(Header(name, 'utf-8').encode(), addr)

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')
ssl = input('ssl yes/no: ')

def _send_with_ssl():
    server = smtplib.SMTP_SSL(smtp_server, PORT_SSL)
    server.starttls()
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

def _send_with_nomral():
    server = smtplib.SMTP(smtp_server, PORT)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

def main():
    msg = MIMEText('hello, send to itabas...', 'plain', 'utf-8')
    msg['From'] = _format_addr('<%s>' % from_addr)
    msg['To'] = _format_addr('<%s>' % to_addr)
    msg['Subject'] = Header('Test python SMTP', 'utf-8').encode()
    msg.attach(MIMEText('send with tumblr file...', 'plain', 'utf-8'))

    with open('%s\tumblr_og2517jYqh1rmxv1to1_540.jpg' % sys.path[0], 'rb') as f:
        mime = MIMEBase('image', 'jpg', filename='test.jpg')
        mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '<0>')
        mime.set_payload(f.read())
        enconders.encode_base64(mime)
        msg.attach(mime)

    if ssl == 'y':
        _send_with_ssl()
    else:
        _send_with_nomral()

main()