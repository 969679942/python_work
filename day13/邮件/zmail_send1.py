import zmail

'''
导包
添加邮件内容,包含主题(subject),正文(content_text),附件(attchments)----一般存储在字典中
添加发件人,包含:发件人账号,密码(授权码)--一般存储在字典中
添加收件人,包含收件人地址,如果有多个收件人则用列表存储
发送邮件
发件人登录:server = zmail.server(username,password)
发件人发送邮件,出入收件人地址,邮件内容 server.send_email(revicer,email_content)
'''
#邮件内容
msg_content={
    'subject':'主题:zmail自动发送测试邮件',
    'content_text':'内容:测试报告',
}
#收件人:如果有多个收件人,则以列表的方式来保存
reviceser = ['3356600581@qq.com','2249334045@qq.com']

#发件人
sender = {'username':'969679942@qq.com','pwd':'nvtasqxmqyqlbfae'}


#发送邮件
server = zmail.server(sender['username'],sender['pwd'])
server.send_mail(reviceser,msg_content)     #把邮件内容发送给收件人

