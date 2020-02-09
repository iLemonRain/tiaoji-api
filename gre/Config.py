#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Config.py    
@Desc    :   
@Project :   py-scripts
@Contact :   thefreer@outlook.com
@License :   (C)Copyright 2018-2020, ZJH567.CN
@WebSite :   zjh567.cn
@Modify Time           @Author        @Version
------------           -------        --------
2020/02/09 17:57       1uvu           1.0         
'''
### 以下为通用的配置，需自己配置

send_email_account = "thefreer@outlook.com" # 用于发送出分通知的邮箱账户和密码
send_email_password = "20202020zz." # 请使用 outlook 等无需进行 SMPTP 或 POP3 授权的邮箱
receive_email_account = "thefreer@163.com" # 如果出分了则发送电子邮件给这个账户
email = {
	'subject': '出分了！', # 邮件标题
	'content_text': '', # 邮件内容
}

### 以下为查询分数需要的信息配置，只需配置自己需要的

# 1. 四川大学配置
scu_config = {
	'id_num': '',  # 身份证号
	'name': ''.encode('utf-8'),  # 名字
	'v_code': 'L626',  # 随便填一个四位的字母和数字， 建议不用改
	'c_num': '',  # 考号 15 位
}


### 以下配置无需更改

# 四川大学
scu_url = "https://yz.scu.edu.cn/score/Query/--"
scu_headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
	'Referer': 'https://yz.scu.edu.cn/score',
	'Content-type': 'application/x-www-form-urlencoded'
}
scu_payload = 'zjhm={}&xm={}&vcode={}&ksbh={}'

# 江苏省院校
jseea_url = "http://stat.jseea.cn/jseea_query/select.do?cid=1"
jseea_headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
}

