from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time

# 不弹出浏览器界面，禁gpu加速
# options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()

# 设置窗口大小
driver.set_window_size(1920, 1080)
# driver.maximize_window()

driver.get("http://www.baidu.com")

# data = driver.find_element_by_id("wrapper").text
# print(data)
# print(driver.title)

driver.find_element_by_id("kw").send_keys("车")
driver.find_element_by_id("su").click()
time.sleep(2)
driver.save_screenshot("车.png")

# 获取html
print(driver.page_source)

cookies = driver.get_cookies()

cookies = {i['name']: i['value'] for i in cookies}

driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("飞机")
driver.find_element_by_id("kw").send_keys(Keys.RETURN)
time.sleep(2)
driver.save_screenshot("飞机.png")

print(driver.current_url)

driver.delete_all_cookies()

driver.quit()


