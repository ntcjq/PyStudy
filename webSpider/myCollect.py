import requests
from bs4 import BeautifulSoup
import re
import socks
import socket

# 设置Socks5代理
# 这里的地址和端口请替换为你的Socks5代理地址和端口
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 7890)
socket.socket = socks.socksocket  # 将Python的socket对象替换为Socks的socket对象


def start():
    for i in range(13):
        index = i + 1
        url = f"https://www.google.com/search?q=python"


def collect():
    url = f"https://www.google.com/search?q=python"
    header = {
    }
    response = requests.get(url, headers=header)
    bs = BeautifulSoup(response.text, features="html.parser")
    # table = bs.find("table", attrs={"class": "jmjoTe"})
    table = bs.find("table")
    trs = table.find_all("tr")
    for t in trs:
        th = t.find("a")
        if th is not None:
            a = th.find("a")
            if a is not None:
                title = a.text
                href = a['href']
                print(title, href)


if __name__ == "__main__":
    collect()
