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
import requests

from gre import Config

class SCU():
	def __init__(self):
		self.flag = "不在可查询时间范围内"
		self.payload = Config.scu_payload.format(
								Config.scu_config['id_num'],
								Config.scu_config['name'],
								Config.scu_config['v_code'],
								Config.scu_config['c_num']
								)
		print("你选择了四川大学查分接口，接口初始化完毕！")
		
	def check(self):
		resp = requests.post(url=Config.scu_url, headers=Config.scu_headers, data=self.payload)
		result = resp.text
		# 如果接收到的电子邮件内容为：验证码错误等其他有用信息，那就是出分了，请快速前往官网查分
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
	

if __name__ == '__main__':
	js = JSEEA()
	result = js.check()
	print(result)