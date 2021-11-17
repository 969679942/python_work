from HtmlTestRunner import HTMLTestRunner
import unittest
import os
from Email import send_mail

tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title = "HKR测试报告",
    description="hkr登录测试报告",
    verbosity=1,
    stream=open(file="hkr.html",mode="w+",encoding="utf-8")
)


runner.run(tests)


# 邮件发送代码
# 4.任务： 使用邮件发送附件，把报告发送给我
send_mail('HKR登录测试','V1.0',['hkr.html','HKR.xls'],['969679942@qq.com',])      #老贾:'2431320433@qq.com'





























































