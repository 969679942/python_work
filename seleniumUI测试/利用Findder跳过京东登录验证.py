# 任务1：
#     京东，搜索一个商品，然后点击添加购物车
# 任务2：
#     2.苏宁的搜索一个商品，然后点击添加购物车。
#     3.b站登陆脚本，然后搜索一个视频，点击播放，点赞。

from selenium import webdriver
import time
import json

driver = webdriver.Chrome()

driver.maximize_window()

# driver.implicitly_wait(2)

driver.get("https://www.jd.com/")

#登陆前,获取cookies
before_login = driver.get_cookies()

driver.find_element_by_xpath("//a[text()='你好，请登录']").click()

driver.find_element_by_xpath("//a[text()='账户登录']").click()

time.sleep(2)

driver.find_element_by_xpath("//input[@id='loginname']").send_keys('15190698685')

driver.find_element_by_xpath("//input[@id='nloginpwd']").send_keys('*****')

time.sleep(2)

driver.find_element_by_xpath("//a[@id='loginsubmit']").click()

#登陆后,获取cookies
after_login = driver.get_cookies()
# 获取 cookies
cookies = driver.get_cookies()
# 将 cookies 写入文件
with open("cookies.txt", "w")  as f:
    json.dump(cookies, f)

time.sleep(54)

driver.quit()
