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

send_email_account = "发件邮箱账户" # 用于发送出分通知的邮箱账户和密码
send_email_password = "发件邮箱密码" # 请使用 outlook 等无需进行 SMPTP 或 POP3 授权的邮箱
receive_email_account = "收件邮箱账户" # 如果出分了则发送电子邮件给这个账户
email = {
	'subject': '出分了！', # 邮件标题
	'content_text': '', # 邮件内容
}

### 以下为查询分数需要的信息配置，只需配置自己需要的
# 1. 四川大学配置
scu_payload = {
	'zjhm': '123456197710016874',  # 身份证号
	'xm': '张三',  # 名字
	'vcode': 'L626',  # 随便填一个四位的字母和数字， 建议不用改
	'ksbn': '123456789012345',  # 考号 15 位
}

# 2. 江苏省考试院：无

# 3. 沈阳师范大学
synu_payload = {
	'cq14s130': '张三', # 姓名
	'cq14s131': '123456789012345' # 身份证号码
}

# 4. 研招网
chsi_payload = {

}

### 以下配置无需更改

# 1. 四川大学
scu_url = "https://yz.scu.edu.cn/score/Query/--"
scu_headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
	'Referer': 'https://yz.scu.edu.cn/score',
	'Content-type': 'application/x-www-form-urlencoded'
}

# 2. 江苏省院校
jseea_url = "http://stat.jseea.cn/jseea_query/select.do?cid=1"
jseea_headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
}

# 3. 沈阳师范大学
synu_url = "http://yjs.synu.edu.cn/_web/commonquery/multipleQueryResult.do?_p=YXM9ODQmdD0yNTgmcD0xJm09TiY_&id=14&mobileTemplate=false"
synu_headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-Requested-With': 'XMLHttpRequest'
}

# 4. 研招网
chsi_url = ""
chsi_headers = {

}

