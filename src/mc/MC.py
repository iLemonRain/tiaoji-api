#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   MC.py
@Desc    :
@Project :   swap
@Contact :   zjh98@vip.qq.com
@License :   (C)Copyright 2018-2020, ZJH
@WebSite :   zjh567.github.io
@Modify Time           @Author        @Version
------------           -------        --------
2020/01/12 23:55       ZJH            1.0
'''
import requests
import pandas as pd
from bs4 import BeautifulSoup

from src.mc import config

class MC(object):
	def __init__(self, payload):
		# payload 格式参见 config 的 index_payload
		self.url = config.url
		self.payload = payload

	def interface(self, page):
		'''
		返回每页的信息列表
		:param page: 页码
		:return: 返回字典的列表
		'''
		self.payload["page"] = page
		resp = requests.get(url=self.url, headers=config.headers, params=self.payload)
		html = resp.text
		info_list = []
		soup = BeautifulSoup(html, "lxml")
		t_soup = soup.select("tbody.forum_body_manage")[0]
		info = {
				'college_name': [],
				'abstract': [],
				'academy_name': [],
				'subject': [],
				'direction': [],
				'mode_name': [],
				'admission_num': [],
				'date': [],
				'description': []
			}
		for idx, tr in enumerate(t_soup.find_all('tr')):
			if idx != 0:
				tds = tr.find_all('td')
				info['college_name'].append(tds[1].text.strip())
				info['abstract'].append(tds[0].text.strip())
				info['academy_name'].append('')
				info['subject'].append(tds[2].text)
				info['direction'].append('')
				info['mode_name'].append('')
				info['admission_num'].append(str(tds[3].text))
				info['date'].append(tds[4].text)
				info['description'].append(self.info_desc(tds[0].a["href"]))
		return info

	def info_desc(self, durl):
		'''
		得到详情页信息
		:param durl: 信息列表中获得的详情页 url
		:return: 补充信息
		'''
		html = requests.get(durl, headers=config.headers).text
		try:
			soup = BeautifulSoup(html, "lxml").select_one("div.t_fsz")
			return str(soup.text.strip())
		except:
			return ""

## 直接运行即可
if __name__ == '__main__':
	mc = MC(config.index_payload)
	info_list =  mc.interface(1)
