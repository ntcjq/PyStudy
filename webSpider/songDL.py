import requests
from bs4 import BeautifulSoup
import time
import json
import random

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

domain = "https://www.gequbao.com"


def search(songName, author):
    # songName = input("请输入歌曲名称：")
    searchUrl = f"{domain}/s/{songName}"
    response = requests.get(searchUrl, headers=headers)
    if response.status_code == 200:
        # 解析HTML内容
        bs = BeautifulSoup(response.text, features="html.parser")
        card = bs.find("div", class_="card-text")
        divs = card.find_all("div", class_="row")
        mp3Id = None
        songNameTemp = None
        authorTemp = None
        fileName = None
        for index, div in enumerate(divs):
            if index != 0:
                a = div.find("a", class_="text-primary font-weight-bold")
                authorDiv = div.find("div", class_="text-success")
                if a is not None:
                    songNameTemp = a.text.strip()
                    mp3Id = a.attrs["href"].split("/")[2]
                if authorDiv is not None:
                    authorTemp = authorDiv.text.strip()
                if authorTemp == author and songNameTemp == songName:
                    fileName = f"{author}-{songName}.mp3"
                    break
        getDownloadUrl(mp3Id, fileName)
    else:
        print(f"请求异常:{author}-{songName}")


def searchByAuthor(author):
    searchUrl = f"{domain}/s/{author}"
    response = requests.get(searchUrl, headers=headers)
    if response.status_code == 200:
        # 解析HTML内容
        bs = BeautifulSoup(response.text, features="html.parser")
        card = bs.find("div", class_="card-text")
        divs = card.find_all("div", class_="row")
        mp3Id = None
        songNameTemp = None
        authorTemp = None
        fileName = None
        for index, div in enumerate(divs):
            if index != 0:
                a = div.find("a", class_="text-primary font-weight-bold")
                authorDiv = div.find("div", class_="text-success")
                if a is not None:
                    songNameTemp = a.text.strip()
                    mp3Id = a.attrs["href"].split("/")[2]
                if authorDiv is not None:
                    authorTemp = authorDiv.text.strip()
                if authorTemp != author:
                    continue
            fileName = f"{author}-{songNameTemp}.mp3"
            getDownloadUrl(mp3Id, fileName)
            delay()
    else:
        print(f"请求异常:{author}-{songName}")


def getDownloadUrl(mp3Id, fileName):
    play_url = f"{domain}/api/play_url?id={mp3Id}&json=1"
    response = requests.get(play_url, headers=headers, timeout=10)
    # 检查请求是否成功
    if response.status_code == 200:
        obj = json.loads(response.content)
        downloadUrl = obj["data"]["url"]
        if downloadUrl is not None:
            download(downloadUrl, fileName)
    else:
        print(f"请求异常:{fileName}")


def download(downloadUrl, fileName):
    response = requests.get(downloadUrl, headers=headers, timeout=10)
    # 检查请求是否成功
    if response.status_code == 200:
        # 打开一个文件来保存下载的内容
        with open(f"C:/Users/Sea/Downloads/music/{fileName}", "wb") as file:
            file.write(response.content)
        print(f"下载成功:{fileName}")
    else:
        print(f"下载失败:{fileName}")


def delay():
    delay = random.uniform(1, 5)  # 生成1到5的随机数
    time.sleep(delay)


if __name__ == "__main__":
    # 按歌名下载
    playList = ["断桥残雪-许嵩", "多余的解释-许嵩"]
    for song in playList:
        info = song.split("-")
        songName = info[0]
        author = info[1]
        search(songName, author)
        delay()

    # 按歌手下载
    # searchByAuthor("许嵩")
