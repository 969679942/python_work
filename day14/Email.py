def send_mail(project_name,version,filename,revicesers):
    import zmail
    # 读取测试报告内容-->文件操作
    # 打开文件
    # file = open('../计算器.html', 'r', encoding='utf-8')
    # msg = file.read()

    # 邮件内容
    msg_content = {
        'subject': '{}项目{}版本自动化测试报告'.format(project_name,version),
        'content_html': '{}项目{}版本自动化测试完毕,具体测试报告请查看附件详情'.format(project_name,version),  # 正文:如果正文需要html格式则为:content_html:msg,正常为content_text
        'attachments': filename


    }
    # 收件人:如果有多个收件人,则以列表的方式来保存--->不确定的
    reviceser = revicesers  # '2249334045@qq.com'

    # 发件人-----固定的
    sender = {'username': '969679942@qq.com', 'pwd': 'nvtasqxmqyqlbfae'}

    # 发送邮件
    server = zmail.server(sender['username'], sender['pwd'])
    server.send_mail(reviceser, msg_content)  # 把邮件内容发送给收件人

# send_mail('测试','v1.0','计算器.html',['969679942@qq.com',])