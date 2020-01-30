#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Notify.py    
@Desc    :   
@Project :   zapis
@Contact :   thefreer@outlook.com
@License :   (C)Copyright 2018-2020, ZJH
@WebSite :   zjh567.cn
@Modify Time           @Author        @Version
------------           -------        --------
2020/01/30 10:14       ZJH            1.0         
'''
import win32gui
import win32con
import winsound

import os
from datetime import datetime


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
		date = datetime.now()
		now = date.strftime("%Y-%m-%d %H-%M-%S").strip()

def test(notify):
	
	msg = '''时间：%s''' % now
	title = "WinNotify"
	notify.showMsg(msg=msg, title=title)
	
if __name__ == '__main__':
    notify = Notify()
    test(notify)