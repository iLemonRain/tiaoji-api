#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   auto.py
@Desc    :   
@Project :   dispensing
@Contact :   thefreer@outlook.com
@License :   (C)Copyright 2018-2020, ZJH
@WebSite :   zjh567.github.io
@Modify Time           @Author        @Version
------------           -------        --------
2020/01/14 17:18       ZJH            1.0         
'''
import threading
import datetime
from datetime import datetime

import win32gui
import win32con
import winsound

import os
import time

# apscheduler 这个模块用来自动下载调度
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.background import BackgroundScheduler



'''
扩展 threading.Thread
使线程可以暂停和恢复
'''
class Thread(threading.Thread):

	def __init__(self, *args, **kwargs):
		super(Thread, self).__init__(*args, **kwargs)
		self.__flag = threading.Event()     # 用于暂停线程的标识
		self.__flag.set()       # 设置为True
		self.__running = threading.Event()      # 用于停止线程的标识
		self.__running.set()      # 将running设置为True

	def run(self):
		date = ""
		while self.__running.isSet():
			self.__flag.wait()      # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
			print("old date is:", date)
			year = datetime.datetime.now().year
			month = datetime.datetime.now().month
			day = datetime.datetime.now().day
			hour = datetime.datetime.now().hour
			minute = datetime.datetime.now().minute
			second = datetime.datetime.now().second
			date = str(year) + "-" + str(month) + "-" + str(day) + "-" + str(hour) + "-" + str(minute) + "-" + str(second)
			print("new date is:", date)
			time.sleep(1)

	def pause(self):
		# 暂停线程调用此方法
		self.__flag.clear()     # 设置为False, 让线程阻塞

	def resume(self):
		# 恢复线程调用此方法
		self.__flag.set()    # 设置为True, 让线程停止阻塞

	def stop(self):
		self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
		self.__running.clear()        # 设置为False


'''
此程序为调用 Windows API 实现发送通知的功能
以下代码无需更改
'''


class Notify():
	def __init__(self):
		# 注册一个窗口类
		wc = win32gui.WNDCLASS()
		hinst = wc.hInstance = win32gui.GetModuleHandle(None)
		self.hover_text = "notify"
		wc.lpszClassName = self.hover_text
		wc.lpfnWndProc = {win32con.WM_DESTROY: self.OnDestroy,}
		classAtom = win32gui.RegisterClass(wc)
		style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
		self.hwnd = win32gui.CreateWindow( classAtom, self.hover_text, style,
				0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,
				0, 0, hinst, None)
		hicon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
		self.nid = (self.hwnd, 0, win32gui.NIF_ICON, win32con.WM_USER+20, hicon, self.hover_text)
		win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, self.nid)

	def showMsg(self, msg="默认消息", title="默认标题", length=200, icon_path="res/custom.ico", ring="res/custom.mp3", hover_text="auto"):
		self.hover_text = hover_text
		hinst = win32gui.GetModuleHandle(None)
		if os.path.isfile(icon_path):
			icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
			hicon = win32gui.LoadImage(hinst,
						icon_path,
						win32con.IMAGE_ICON,
						0,
						0,
						icon_flags)
		else:
			print("Can't find icon file - using default.")
			hicon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)

		if self.nid: message = win32gui.NIM_MODIFY
		else: message = win32gui.NIM_ADD
		win_tag = win32gui.NIF_INFO | win32gui.NIF_ICON | win32gui.NIF_TIP | win32gui.NIF_MESSAGE
		self.nid = (self.hwnd,
					0,
					win_tag,
					win32con.WM_USER+20,
					hicon,
					self.hover_text,
					msg,
					length,
					title
					# hicon
					)
		win32gui.Shell_NotifyIcon(message, self.nid)
		# 此处可根据hover_text播放不同的铃声
		self.playSound(ring)


	def playSound(self, ring):
		try:
			winsound.PlaySound(ring, winsound.SND_ASYNC)
		except:
			pass

	def OnDestroy(self, hwnd, msg, wparam, lparam):
		nid = (self.hwnd, 0)
		win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, nid)
		win32gui.PostQuitMessage(0) # Terminate the app.

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
	def func():
		print("调度成功。。。")

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
	args = []
	# 初始化自动下载线程对象
	adt = Download(func, trigger_config, args)
	# 运行线程
	adt.start()
