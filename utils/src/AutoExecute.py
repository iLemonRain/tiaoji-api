#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Auto.py
@Desc    :   
@Project :   dispensing
@Contact :   thefreer@outlook.com
@License :   (C)Copyright 2018-2020, ZJH
@WebSite :   zjh567.github.io
@Modify Time           @Author        @Version
------------           -------        --------
2020/01/14 17:18       ZJH            1.0         
'''
import time
from datetime import datetime
from threading import Thread

# apscheduler 这个模块用来自动下载调度
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.background import BackgroundScheduler


class Download(Thread):
	'''
	这个类是一个自 动运行下载程序的线程类，继承自 AutoThread.Thread
	此线程类的 run 方法用于运行上面的 AutoDownApp 对象
	'''
	
	def __init__(self, func, trigger_config, args=None):
		super(Download, self).__init__()
		# 初始化一个调度器对象
		self.scheduler = BackgroundScheduler()
		# 初始化一个触发器对象，其中 trigger_config 为触发器的配置，用于配置何时触发行为
		self.trigger = CronTrigger(**trigger_config)
		# 初始化调度器的配置
		self.config = {
			"func": func,  # 运行的函数，AutoDownApp.download，即自动下载
			"args": args,  # 运行函数时需传入的参数，形式为列表
			"trigger": self.trigger,  # 触发器对象
		}
	
	def run(self):
		'''
		此 run 方法为运行线程时执行的过程
		此方法无需显式的调用，如声明了一个线程：
			t = AutoDownThread(**config)
		那么只需：
			t.start()
		线程就会执行这个 run 函数
		可根据你的需求重载这个 run 函数
		:return: 无
		'''
		# 根据调度器配置添加一个调度任务，用于执行一些动作
		# 一个调度器可以添加多个任务
		self.scheduler.add_job(**self.config)
		# 执行调度器
		self.scheduler.start()
		# 下面这个 while 循环保证调度器永远运行
		while True:
			time.sleep(600)

if __name__ == "__main__":
	def func(now):
		print("%s: 调度成功... " % now)

	# 触发器配置
	trigger_config = {
        "year": "*",
        "month": "*",
        "day": "*",
        "hour": "*",
        "minute": "*",
        "second": "0,10,20,30,40,50",
        "week": "*",
        "day_of_week": "*"
    }
	# 回调函数参数
	date = datetime.now()
	now = date.strftime("%Y-%m-%d %H-%M-%S").strip()
	args = [now, ]
	# 初始化自动下载线程对象
	download = Download(func, trigger_config, args)
	# 运行线程
	download.start()
