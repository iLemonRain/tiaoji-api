#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo.py    
@Desc    :   
@Project :   dispensing
@Contact :   thefreer@outlook.com
@License :   (C)Copyright 2018-2020, ZJH
@WebSite :   zjh567.github.io
@Modify Time           @Author        @Version
------------           -------        --------
2020/01/14 18:49       ZJH            1.0         
'''
import pandas as pd
from datetime import datetime

from src.mc.MC import MC
import src.mc.config as mc_config
from src.yl.YL import YL
import src.yl.config as yl_config


def func(obj, root='./', ran=(1,10)):
	if list(root)[-1] != '/':
		root += '/'
	date = datetime.now()
	now = date.strftime("%Y-%m-%d %H-%M-%S").strip()
	
	df = pd.DataFrame()
	for i in range(ran[0], ran[1]):
		info = obj.interface(i)
		print(info)
		df_t = pd.DataFrame(info)
		df = pd.concat([df, df_t], ignore_index=True)
		
	df.to_excel("./%s%s" % (root, now) + ".xlsx")
	msg = '''时间：%s  结果：下载完成''' % now
	print(msg)
	
if __name__ == '__main__':
	mc = MC(mc_config.index_payload)
	yl = YL(yl_config.dispensing_payload)
	root = './output'
	ran = (1, 5)
	# 回调函数参数
	func(mc, root, ran)

