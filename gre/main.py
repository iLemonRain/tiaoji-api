#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Desc    :   
@Project :   py-scripts
@Contact :   thefreer@outlook.com
@License :   (C)Copyright 2018-2020, ZJH567.CN
@WebSite :   zjh567.cn
@Modify Time           @Author        @Version
------------           -------        --------
2020/02/09 18:30       1uvu           1.0         
'''
# 四川大学
from gre.src.Score import SCU
from gre.src.Utils import emailNotify, randomSleep

if __name__ == '__main__':
	scu = SCU()
	while True:
		result = scu.check()
		if result:
			emailNotify(result)
		randomSleep(time_seed=2)

# ## 江苏省
# from gre.src.Score import JSEEA
# from gre.src.Utils import emailNotify, randomSleep
#
# if __name__ == '__main__':
# 	jseea = JSEEA()
# 	while randomSleep(time_seed=2):
# 		result = jseea.check()
# 		if result:
# 			emailNotify(result)
