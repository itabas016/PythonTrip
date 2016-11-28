#/usr/bin/env python
#coding=utf8
import httplib
import hashlib
import urllib
import random
import urllib2
import md5
import re
import json
import sys
import time
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from newspaper import Article
reload(sys)
sys.setdefaultencoding('utf-8')
time1 = time.time()
#得到html的源码
def gethtml(url1):
    #伪装浏览器头部
    headers = {
       'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib2.Request(
    url = url1,
    headers = headers
    )
    html = urllib2.urlopen(req).read()
    return html
#得到目标url源码
code1 = gethtml('https://www.baidu.com')#示例
#提取内容
content1 = re.findall('<h2 class="title"><a href="(.*)">(.*)</a></h2>',code1)#示例
#追加记录采集来的内容
f1 = open('contents1.txt','a+')
#读取txt中的内容
exist1 = f1.read()



def sends():
    for i in range(len(content1)):
        u=content1[i][0]
        url='https://www.baidu.com'+u
        a=Article(url,language='zh')
        a.download()
        a.parse()
        dst=a.text
        title=a.title
   
        #链接WordPress，输入xmlrpc链接，后台账号密码
        wp = Client('weburl/xmlrpcurl/xmlrpc.php','username','password')
		#示例：wp = Client('http://www.python-cn.com/xmlrpc.php','username','password')
        post = WordPressPost()
        post.title = title
        post.content = dst
        post.post_status = 'publish'
        #发送到WordPress
        wp.call(NewPost(post))
        time.sleep(3)
        print 'posts updates'

if __name__=='__main__':
    sends()
    f1.close()