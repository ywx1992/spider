from selenium import webdriver
import time
import requests
from yundama.dama import indentify


class Douban(object):
    def __init__(self):
        self.url = "https://www.douban.com/"
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element_by_name("form_email").send_keys("15692092379")
        self.driver.find_element_by_id("form_password").send_keys("15692092379")

        # 处理验证码
        captcha_url = self.driver.find_element_by_id("captcha_image").get_attribute("src")
        captcha_content = requests.get(captcha_url).content
        # with open("captcha.jpg", "wb") as f:
        #     f.write(captcha_content)
        # captcha_code = input("请输入验证码：")

        captcha_code = indentify(captcha_content)
        self.driver.find_element_by_id("captcha_field").send_keys(captcha_code)
        time.sleep(3)
        self.driver.find_element_by_class_name("bn-submit").click()
        time.sleep(3)
        self.driver.save_screenshot("豆瓣.png")
        print(self.driver.get_cookies())
        cookies = {i["name"]: i["value"] for i in self.driver.get_cookies()}
        print(cookies)

        # self.driver.quit()

    # def __del__(self):
    #     self.driver.quit()


if __name__ == "__main__":
    d = Douban()
    d.login()




# //input[@id='form_email']
#
# //input[@id='form_password']
#
# 15692092379