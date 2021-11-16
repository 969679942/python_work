import json
from time import sleep
from selenium import webdriver

# from selenium.webdriver.common.keys import keys

# 初始化浏览器
driver = webdriver.Chrome()

# 定义全局遍变量url
url = "https://www.jd.com"


def login_coolie():
    # 打开浏览器
    driver.get(url)
    # 浏览器最大化
    driver.maximize_window()
    # 定位登录button
    driver.find_element_by_class_name("link-login").click()
    # 定位账户登录
    driver.find_element_by_xpath('//a[text()="账户登录"]').click()
    # 定位账号框，并输入账号
    driver.find_element_by_xpath('//input[@name="loginname"]').send_keys("15190698685")
    # 定位密码框，并输入密码
    driver.find_element_by_xpath('//input[@type="password"]').send_keys("*******")
    # 点击登录button
    driver.find_element_by_xpath('//a[@id="loginsubmit"]').click()
    sleep(5)
    # 需要手动滑动图片，通过校验

    # 获取coolie
    my_coolie = driver.get_cookies()
    print(my_coolie)
    data_cookie = json.dumps(my_coolie)
    with open("jd_coolies", "w") as fp:
        fp.write(data_cookie)


# 使用cookies
def get_url_with_cookies():
    # 访问网站，清空旧cookies信息
    driver.get(url)
    driver.delete_all_cookies()
    # 获取cookies文件
    with open("jd_coolies", "r") as fp:
        jd_cookies = fp.read()
    # 加载cookies信息
    jd_cookies_dict = json.loads(jd_cookies)
    for cookie in jd_cookies_dict:
        driver.add_cookie(cookie)
    # 验证是否登录成功
    driver.get(url)
    print(url)


if __name__ == "__main__":
    # login_coolie()
    get_url_with_cookies()