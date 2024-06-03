import requests
from bs4 import BeautifulSoup
import re
import time

domain = ""

cookies = {}

proxy = {"http": "127.0.0.1:7890", "https": "127.0.0.1:7890"}

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}


def start():
    for i in range(1):
        page = i + 1 + 10
        collect(str(page))
        time.sleep(2)  # 休眠2秒钟


def collect(page):

    timestamp = int(round(time.time() * 1000))
    # print(timestamp)
    url = (
        domain
        + "/my/favourites/videos/?mode=async&function=get_block&block_id=list_videos_my_favourite_videos&fav_type=0&playlist_id=0&sort_by=&from_my_fav_videos="
        + page
        + "&_="
        + str(timestamp)
    )
    # print(url)

    response = requests.get(url, cookies=cookies, proxies=proxy, headers=header)
    bs = BeautifulSoup(response.text, features="html.parser")
    divF = bs.find("div", attrs={"class": "gutter-20"})
    boxes = divF.find_all("div", attrs={"class": "video-img-box"})
    for box in boxes:
        detailDiv = box.find("div", attrs={"class": "detail"})
        if detailDiv is not None:
            a = detailDiv.find("a")
            if a is not None:
                title = a.text
                href = a["href"]
                print(title)


if __name__ == "__main__":
    start()
