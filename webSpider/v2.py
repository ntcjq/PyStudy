import requests
from bs4 import BeautifulSoup


def main():
    header = {}
    proxy = {"http":"127.0.0.1:1087","https":"127.0.0.1:1087"}
    header[
        'User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    req = requests.get("https://www.v2ex.com/",headers=header,proxies=proxy)
    bs = BeautifulSoup(req.text, features="html.parser")
    
    divs = bs.find_all("div",class_="cell item")
    for div in divs:
        a = div.find("a",class_="topic-link")
        print(a.text)
        print(f"https://www.v2ex.com"+a['href'])

if __name__ == "__main__":
    main()