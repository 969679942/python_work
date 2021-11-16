from selenium import webdriver
import time
import random

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.bilibili.com/")
time.sleep(5)
search = driver.find_element_by_xpath("//form[@id='nav_searchform']/input")
search.clear()
search.send_keys('武松')

driver.find_element_by_xpath("//div[@class='nav-search-btn']/button").click()

driver.switch_to.window(driver.window_handles[1])

#将搜索到的当前页面视频,返回一个list列表
lists = driver.find_elements_by_xpath("//li[@class='video-item matrix']/a")
count = random.randint(0,19)
#调用JS代码,滚动页面,让指定元素在页面中出现
driver.execute_script('arguments[0].scrollIntoView();',lists[19])

lists[19].click()

time.sleep(5)

