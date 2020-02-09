#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Score.py    
@Desc    :   
@Project :   py-scripts
@Contact :   thefreer@outlook.com
@License :   (C)Copyright 2018-2020, ZJH567.CN
@WebSite :   zjh567.cn
@Modify Time           @Author        @Version
------------           -------        --------
2020/02/09 18:21       1uvu           1.0         
'''
import json
import requests
from urllib import parse

from gre import Config

class SCU():
	def __init__(self):
		self.flag = "不在可查询时间范围内"
		self.payload = parse.urlencode(Config.scu_payload)
		print("你选择了四川大学查分接口，接口初始化完毕！")
		
	def check(self):
		resp = requests.post(url=Config.scu_url, headers=Config.scu_headers, data=self.payload)
		result = resp.text
		if self.flag not in result:
			return False
		return result
	
class JSEEA():
	def __init__(self):
		self.flag = "2019年研究生考试成绩"
		print("你选择了江苏省考试院查分接口，接口初始化完毕！")
	
	def check(self):
		resp = requests.get(url=Config.jseea_url, headers=Config.jseea_headers)
		result = resp.text
		if self.flag in result:
			return False
		return result

class SYNU():
	def __init__(self):
		self.flag = "\\u62b1\\u6b49\\uff0c\\u6ca1\\u6709\\u60a8\\u60f3\\u8981\\u7684\\u67e5\\u8be2\\u7ed3\\u679c\\uff0c\\u8bf7\\u4ed4\\u7ec6\\u6838\\u5bf9\\u60a8\\u7684\\u8f93\\u5165\\u662f\\u5426\\u6b63\\u786e\\uff01"
		self.payload = parse.urlencode(Config.synu_payload)
		print("你选择了沈阳师范大学查分接口，接口初始化完毕！")
	
	def check(self):
		resp = requests.post(url=Config.synu_url, headers=Config.synu_headers, data=self.payload)
		js = json.loads(resp.text)
		result = js[0]
		if self.flag in result["displayContent"]:
			return False
		return result

if __name__ == '__main__':
	s = SYNU()
	result = s.check()
	print(result)
