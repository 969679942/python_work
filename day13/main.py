'''
    1.加载所有的测试用例
    2.执行用例并生成测试报告
'''

import unittest
from Email import send_mail

# 1.加载所有用例
from HtmlTestRunner import HTMLTestRunner

tests = unittest.defaultTestLoader.discover(r"C:\Users\Administrator\Desktop\python课程\day13【单元测试】\代码\day13",pattern="Test*.py")

# 2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "计算器的测试报告",
    description="这是加法测试报告",
    verbosity=1,
    stream = open(file="计算器.html",mode="w+",encoding="utf-8")
)

# 3.执行用例
runner.run(tests)




# 4.任务： 使用邮件发送附件，把报告发送给我
send_mail('计算器测试','V1.0','计算器.html',['2431320433@qq.com','969679942@qq.com'])




