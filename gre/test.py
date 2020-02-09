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

url = "http://yjs.synu.edu.cn/_web/commonquery/multipleQueryResult.do?_p=YXM9ODQmdD0yNTgmcD0xJm09TiY_&id=14&mobileTemplate=false"

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-Requested-With': 'XMLHttpRequest'
}

payload = "cq14s130=%E5%BC%A0%E5%BB%BA%E8%BE%89&cq14s131=152326199810016895"

resp = requests.post(url=url, headers=headers, data=payload)
print(resp.text)

