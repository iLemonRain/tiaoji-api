#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Utils.py
@Desc    :   
@Project :   py-scripts
@Contact :   thefreer@outlook.com
@License :   (C)Copyright 2018-2020, ZJH567.CN
@WebSite :   zjh567.cn
@Modify Time           @Author        @Version
------------           -------        --------
2020/02/09 17:56       1uvu           1.0         
'''
import random
import time
import zmail

from gre import Config

def emailNotify(content_text):
	try:
		server = zmail.server(Config.send_email_account, Config.send_email_password)
		Config.email["content_text"] = content_text
		server.send_mail(Config.receive_email_account, Config.email)  # 如果出分了则发送电子邮件给这个账户
		print("发送成功")
	except:
		print("发送失败")
		

def randomSleep(time_seed=2):
	'''
	随即睡眠 time_seed ~ time_seed + 1 分钟
	:param time_seed: 时间种子，1 代表 1 分钟
	:return:
	'''
	time.sleep(random.randint(time_seed*60, time_seed*60+60))
	return True
	