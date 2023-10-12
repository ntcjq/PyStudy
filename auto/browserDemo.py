from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
#执行完不关闭浏览器
options.add_experimental_option('detach', True)
#最大化界面
options.add_argument("--start-maximized")
#无UI界面运行
# options.add_argument("--headless")


def main():
    browser = webdriver.Chrome(options)
    #隐式等待
    browser.implicitly_wait(5)
    #打开百度
    browser.get('http://www.baidu.com/')
    #找到输入框
    elem = browser.find_element(By.ID, 'kw')

    #清空内容
    elem.clear()
    #输入内容并回车
    elem.send_keys('java' + Keys.ENTER)

    #强制等待
    # time.sleep(3)

    browser.find_element(By.LINK_TEXT, "又见长江").click()

    print(browser.current_url)

    #获取Html
    html = browser.page_source
    bf = BeautifulSoup(html, features="html.parser")
    divs = bf.find_all("div")
    print(len(divs))
    #点击搜索
    # browser.find_element(By.ID, 'su').click()

    #关闭浏览器
    # browser.quit()
    #关闭当前tab
    # browser.close()


if __name__ == '__main__':
    main()
