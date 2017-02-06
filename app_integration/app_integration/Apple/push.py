#coding=utf-8

from applepush import ApplePush

apns = ApplePush('证书文件名称', 'bundle ID')
resp = apns.single_push('苹果设备token', "推送内容")