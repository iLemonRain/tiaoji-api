#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py    
@Desc    :   
@Project :   zapis
@Contact :   thefreer@outlook.com
@License :   (C)Copyright 2018-2020, ZJH567.CN
@WebSite :   zjh567.cn
@Modify Time           @Author        @Version
------------           -------        --------
2020/02/09 20:19       1uvu           1.0         
'''
import requests


headers = {

}

name = "张建辉".encode('utf-8')
payload = "" % name

resp = requests.post(url=url, headers=headers, data=payload)
print(resp.text)

