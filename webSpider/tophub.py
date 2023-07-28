from bs4 import BeautifulSoup
import requests
import re


def news():
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    session = requests.session()
    session.cookies.set("Hm_lpvt_3b1e939f6e789219d8629de8a519eab9",
                        "1690467681")
    session.cookies.set("Hm_lvt_3b1e939f6e789219d8629de8a519eab9",
                        "1690459984")
    req = session.get("https://tophub.today/", headers=headers)
    bs = BeautifulSoup(req.text, features="html.parser")
    sortables = bs.find_all("div", id='Sortable')
    #第二行
    contents = sortables[1].find_all("div", class_="nano-content")
    for content in contents:
        aarr = content.find_all("a")
        print("=" * 30)
        for idx in range(len(aarr)):
            news = aarr[idx].find("span", class_="t").text
            print("%s.%s" % (idx + 1, news))


if __name__ == "__main__":
    news()