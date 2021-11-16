# 任务1：
#     京东，搜索一个商品，然后点击添加购物车
# 任务2：
#     2.苏宁的搜索一个商品，然后点击添加购物车。
#     3.b站登陆脚本，然后搜索一个视频，点击播放，点赞。

from selenium import webdriver
import time
import cv2
import numpy as np
from urllib import request
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
def getPic():
    # 用于找到登录图片的大图
    s2 = r'//div/div[@class="JDJRV-bigimg"]/img'
    # 用来找到登录图片的小滑块
    s3 = r'//div/div[@class="JDJRV-smallimg"]/img'
    bigimg = driver.find_element_by_xpath(s2).get_attribute("src")
    smallimg = driver.find_element_by_xpath(s3).get_attribute("src")
    # print(smallimg + '\n')
    # print(bigimg)
    # 背景大图命名
    backimg = "backimg.png"
    # 滑块命名
    slideimg = "slideimg.png"
    # 下载背景大图保存到本地
    request.urlretrieve(bigimg, backimg)
                                                    #压缩背景图片成为登录网页大小规格的图片:278 x 108.11
    img = Image.open('backimg.png')
    out = img.resize((278, 108), Image.ANTIALIAS)  # resize image with high-quality
    out.save('backimg.png', 'png')

    # 下载滑块保存到本地
    request.urlretrieve(smallimg, slideimg)
                                                    # 压缩滑块图片成为登录网页大小规格的图片:38.61 x 38.61
    img = Image.open('slideimg.png')
    out = img.resize((38, 38), Image.ANTIALIAS)  # resize image with high-quality
    out.save('slideimg.png', 'png')

    # 获取图片并灰度化
    block = cv2.imread(slideimg, 0)
    template = cv2.imread(backimg, 0)
    # 二值化后的图片名称
    blockName = "block.jpg"
    templateName = "template.jpg"
    # 将二值化后的图片进行保存
    cv2.imwrite(blockName, block)
    cv2.imwrite(templateName, template)
    block = cv2.imread(blockName)
    block = cv2.cvtColor(block, cv2.COLOR_RGB2GRAY)
    block = abs(255 - block)
    cv2.imwrite(blockName, block)
    block = cv2.imread(blockName)
    template = cv2.imread(templateName)
    # 获取偏移量
    result = cv2.matchTemplate(block, template, cv2.TM_CCOEFF_NORMED) # 查找block在template中的位置，返回result是一个矩阵，是每个点的匹配结果
    print(result)
    print(result.argmax(),result.shape)
    x, y = np.unravel_index(result.argmax(), result.shape)
    print("x方向的偏移", int(y * 0.4 + 18), 'x:', x, 'y:', y)
    # print("x方向的偏移", int(y * 0.4 + 18), 'x:', x, 'y:', y)
    # 获取滑块
    element = driver.find_element_by_xpath(s3)
    ActionChains(driver).click_and_hold(on_element=element).perform()
    ActionChains(driver).move_to_element_with_offset(to_element=element, xoffset=y, yoffset=0).perform()
    ActionChains(driver).release(on_element=element).perform()
    time.sleep(3)


driver = webdriver.Chrome()

driver.maximize_window()

# driver.implicitly_wait(6)

driver.get("https://www.jd.com/")

driver.find_element_by_xpath("//a[text()='你好，请登录']").click()

driver.find_element_by_xpath("//a[text()='账户登录']").click()

driver.find_element_by_xpath("//input[@id='loginname']").send_keys('15190698685')

driver.find_element_by_xpath("//input[@id='nloginpwd']").send_keys('****')

time.sleep(2)

driver.find_element_by_xpath("//a[@id='loginsubmit']").click()

time.sleep(4)

while True:
    try:
        getPic()
    except Exception as e:
        print(e)
        break

time.sleep(5)

driver.quit()

