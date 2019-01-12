from selenium import webdriver
import json
import time


class Douyu(object):
    def __init__(self):
        self.url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)  # 发送首页请求

    def get_content(self):
        time.sleep(2)  # 每次发送请求后等待2秒，等待页面加载完成
        li_list = self.driver.find_elements_by_xpath("//a[@class='play-list-link']")
        content_list = []
        for i in li_list:
            image = i.find_element_by_xpath("./span/img").get_attribute("src")  # 封面图
            title = i.find_element_by_xpath("./div/div/h3").text  # 房间名
            category = i.find_element_by_xpath("./div/div/span").text  # 直播分类
            name = i.find_element_by_xpath("./div/p/span[1]").text  # 主播名
            number = i.find_element_by_xpath("./div/p/span[2]").text  # 观看人数

            content = {
                "房间封面": image,
                "房间名": title,
                "直播分类": category,
                "主播名": name,
                "观看人数": number,
            }
            content_list.append(content)

        # 获取下一页url
        next_url = self.driver.find_elements_by_class_name("shark-pager-next")
        next_url = next_url[0] if len(next_url) > 0 else None

        return content_list, next_url

    def save_content(self, content_list):
        f = open("douyu__.json", "a")
        for content in content_list:
            json.dump(content, f, ensure_ascii=False)
            f.write("\n")
        f.close()

    def run(self):
        # 发送首页请求，获取内容并保存
        content_list, next_url = self.get_content()
        self.save_content(content_list)

        # 点击下一页，直到不能点

        while next_url is not None:
            next_url.click()
            content_list, next_url = self.get_content()
            self.save_content(content_list)

        print("保存成功")


if __name__ == "__main__":
    d = Douyu()
    d.run()


# "https://www.douyu.com/directory/all"
# //a[@class='play-list-link']
#
# /span/img/@src #封面
#
# /div/div/h3 #title标题
#
# /div/div/span # 直播分类
#
# /div/p/span[1] #主播名
#
# /div/p/span[2] #观看人数
#
# //a[@class='shark-pager-next'] #下一页
#
# //a[contains(@class, 'shark-pager-disable-next')] #最后一页