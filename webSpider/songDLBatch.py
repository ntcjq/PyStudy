import requests
from bs4 import BeautifulSoup
import time
import json
import random

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

domain = "https://www.gequbao.com"


def search(songName):

    searchUrl = domain + "/s/"
    # songName = input("请输入歌曲名称：")
    searchUrl += songName
    response = requests.get(searchUrl, headers=headers)
    if response.status_code == 200:
        # 解析HTML内容
        bs = BeautifulSoup(response.text, features="html.parser")
        card = bs.find("div", class_="card-text")
        if card is not None:
            divs = card.find_all("div", class_="row")
            for index, div in enumerate(divs):
                if index == 1:
                    songName = ""
                    mp3Id = None
                    a = div.find("a", class_="text-primary font-weight-bold")
                    authorDiv = div.find("div", class_="text-success")
                    if authorDiv is not None:
                        author = authorDiv.text.strip() + "-"
                        songName = author
                    if a is not None:
                        songName += a.text.strip() + ".mp3"
                        mp3Id = a.attrs["href"].split("/")[2]
                    getDownloadUrl(mp3Id, songName)

    else:
        print("无法搜索到该歌曲:", songName)


def getDownloadUrl(mp3Id, songName):
    play_url = domain + "/api/play_url?id=" + mp3Id + "&json=1"
    response = requests.get(play_url, headers=headers, timeout=10)
    # 检查请求是否成功
    if response.status_code == 200:
        obj = json.loads(response.content)
        downloadUrl = obj["data"]["url"]
        print(songName, "", downloadUrl)
        download(downloadUrl, songName)
    else:
        print("无法下载到该歌曲:", songName)


def download(downloadUrl, name):
    response = requests.get(downloadUrl, headers=headers, timeout=10)
    # 检查请求是否成功
    if response.status_code == 200:
        # 打开一个文件来保存下载的内容
        with open("C:/Users/Sea/Downloads/music/" + name, "wb") as file:
            file.write(response.content)
        print(name + " 下载成功！")
    else:
        print("无法下载到该歌曲:", name)


def delay():
    delay = random.uniform(1, 5)  # 生成1到5的随机数
    time.sleep(delay)


if __name__ == "__main__":
    false = False
    true = True
    playList = [
       
    ]
    for song in playList:
        delay()
        search(song)
