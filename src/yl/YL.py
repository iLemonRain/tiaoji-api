#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   YL.py    
@Desc    :   
@Project :   yl
@Contact :   thefreer@outlook.com
@License :   (C)Copyright 2018-2020, ZJH
@WebSite :   zjh567.github.io
@Modify Time           @Author        @Version
------------           -------        --------
2020/01/14 11:31       ZJH            1.0         
'''
import json

import requests
from src.yl import config


class YL(object):
	def __init__(self, payload):
		# payload 格式参见 config 的 dispensing_payload
		self.college_url = config.college_url
		self.dispensing_url = config.dispensing_url
		self.payload = payload
		
	def college_list(self, province):
		'''
		输入省份，返回省份大学列表：ID，名字
		:param province: 省份名字，如：四川、内蒙古、重庆等等
		:return: 大学列表，列表元素为大学信息字典
		'''
		resp = requests.get(url=self.college_url + province, headers=config.headers)
		html = resp.text
		js = json.loads(html)
		data = js["data"]
		return data
	
	
	def yl_interface(self, page):
		'''
		根据 payload，返回查到的调剂信息
		:param page: 页码
		:return: 信息列表
		'''
		self.payload["page"] = page
		resp = requests.get(url=self.dispensing_url, headers=config.headers, params=self.payload)
		html = resp.text
		js = json.loads(html)
		data = js["data"]["data"]
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
		for d in data:
			info['college_name'].append(d["college_name"])
			info['abstract'].append('')
			info['academy_name'].append(d["academy_name"])
			info['subject'].append(d["category"] + " -> " + d["first_subjects"] + " -> " + d["major_name"])
			info['direction'].append(d["direction"])
			info['mode_name'].append(d["mode_name"])
			info['admission_num'].append(str(d["admission_num"]))
			info['date'].append(d["year"])
			info['description'].append('')
		return info
	

## 直接运行即可
if __name__ == '__main__':
	yl = YL(config.dispensing_payload)
	p = "安徽"
	# print(yl.college_list(p))
	print(yl.yl_interface(1))
	

