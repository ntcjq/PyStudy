from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time


# 创建Chrome选项对象
chrome_options = Options()

# 禁用图形界面
chrome_options.add_argument("--headless")

# 初始化WebDriver
driver = webdriver.Chrome(options=chrome_options)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}


def search(songName):
    domain = "https://www.gequbao.com"
    searchUrl = domain + "/s/"
    # 获取歌曲名称
    # songName = input("请输入歌曲名称：")
    # 拼接搜索URL
    searchUrl += songName
    # 发送GET请求
    response = requests.get(searchUrl, headers=headers)
    if response.status_code == 200:
        # 解析HTML内容
        bs = BeautifulSoup(response.text, features="html.parser")
        card = bs.find("div", class_="card-text")
        divs = card.find_all("div", class_="row")
        for index, div in enumerate(divs):
            if index == 1:
                a = div.find("a", class_="text-primary font-weight-bold")
                if a is not None:
                    downloadPageUrl = domain + a.attrs["href"]
                    downloadPage(downloadPageUrl)

    else:
        print("无法搜索到该歌曲。状态码:", response.status_code)


def downloadPage(downloadPageUrl):
    # 打开下载页面
    driver.get(downloadPageUrl)
    # 点击下载按钮
    # 确定元素是可点击的
    button_locator = driver.find_element(
        By.ID, "btn-download-mp3"
    )  # 假设按钮有一个ID为'button_id'
    wait = WebDriverWait(driver, 10)
    button = wait.until(element_to_be_clickable(button_locator))
    # 点击按钮
    button.click()
    time.sleep(1)
    aButton = driver.find_element(By.LINK_TEXT, "下载低品质MP3")
    downloadUrl = aButton.get_attribute("href")
    name = aButton.get_attribute("download")
    print(name, "", downloadUrl)
    driver.quit()
    # download(downloadUrl, name)


def download(downloadUrl, name):
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    }
    # 发送GET请求
    response = requests.get(downloadUrl, headers=headers, timeout=10)
    # 检查请求是否成功
    if response.status_code == 200:
        # 打开一个文件来保存下载的内容
        with open(name, "wb") as file:
            file.write(response.content)
        print("歌曲下载成功！")
    else:
        print("无法下载歌曲。状态码:", response.status_code)


if __name__ == "__main__":
    author = "多余的解释"
    search(author)
