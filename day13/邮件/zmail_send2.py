'''
html内容写在一个content.html的文件中
导报:import zmail
读取content.html文件内容:with opem(filename,mode) as f 或者file=open(filename,mode)\
添加邮件内容,包含主题(subject),正文(content_text),附件(attachments)----一般存储在字典中
添加发件人,包含:发件人账号,密码(授权码)--一般存储在字典中
添加收件人,包含收件人地址,如果有多个收件人则用列表存储
发送邮件
发件人登录:server = zmail.server(username,password)
发件人发送邮件,出入收件人地址,邮件内容 server.send_email(revicer,email_content)
'''
import zmail
#读取测试报告内容-->文件操作
#打开文件
file = open('../计算器.html','r',encoding='utf-8')
msg = file.read()


#邮件内容
msg_content={
    'subject':'主题:zmail自动发送测试邮件',
    'content_html':msg,                 #正文:如果正文需要html格式则为:content_html:msg,正常为content_text
    'attachments':['../计算器.html','a.html']  #Header 'attchments' is invalid and unused,if you want to add extra headers use 'headers' instead.

}
#收件人:如果有多个收件人,则以列表的方式来保存
reviceser = ['969679942@qq.com',] #'2249334045@qq.com'

#发件人
sender = {'username':'969679942@qq.com','pwd':'nvtasqxmqyqlbfae'}


#发送邮件
server = zmail.server(sender['username'],sender['pwd'])
server.send_mail(reviceser,msg_content)     #把邮件内容发送给收件人

