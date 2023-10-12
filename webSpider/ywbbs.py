import requests
from bs4 import BeautifulSoup
import re


def start():
    for i in range(13):
        index = i + 1
        url = f"http://bbs.212300.com/forum-88-{index}.html"
        getTitles(url)


def getTitles(url):
    header = {
        "Cookie":
        "X_CACHE_KEY=ada592d39fc8a8186e6a785ce8bd89af; __51vcke__JiBDr7eQ3TiR5eYF=ee301312-544a-552e-8a5c-51571d18e491; __51vuft__JiBDr7eQ3TiR5eYF=1681976110316; __51huid__JqojczetbdWSNVAA=aac5943a-e56a-58a3-bfa8-6c758b86d6b4; kdFj_5289_saltkey=buFsyZ9h; kdFj_5289_lastvisit=1691569263; kdFj_5289_seccode=69.4cd6dbb3259f65842d; kdFj_5289_ulastactivity=1691572901%7C0; kdFj_5289_auth=58afE%2FeewPlnxKN%2FVNcQrRshJbTNvr8SfwD6Mfqgry4v2CsodwnHpHFI7aa7s3b5lvI8FB5Fyzg1r4%2Fzvy5zy3Sd%2Bd5Z; kdFj_5289_lastcheckfeed=1944676%7C1691572901; kdFj_5289_lip=27.115.120.10%2C1691572901; kdFj_5289_connect_is_bind=0; __51uvsct__JiBDr7eQ3TiR5eYF=2; kdFj_5289_noticeTitle=1; kdFj_5289_nofavfid=1; kdFj_5289_st_p=1944676%7C1691572968%7Cbd0f632ccbc360c47b0a6de135e64945; kdFj_5289_viewid=tid_6706869; kdFj_5289_smile=2D1; kdFj_5289_visitedfid=88D68; kdFj_5289_st_t=1944676%7C1691573421%7Cdf3b320cebb72278456d9abbbcbb4332; kdFj_5289_forum_lastvisit=D_88_1691573421; __vtins__JiBDr7eQ3TiR5eYF=%7B%22sid%22%3A%20%22ebce7228-bcb2-52d9-acd9-1f197e5878f9%22%2C%20%22vd%22%3A%208%2C%20%22stt%22%3A%20494581%2C%20%22dr%22%3A%206335%2C%20%22expires%22%3A%201691575221932%2C%20%22ct%22%3A%201691573421932%7D; kdFj_5289_lastact=1691573662%09forum.php%09ajax"
    }
    req = requests.get(url, headers=header)
    bs = BeautifulSoup(req.text, features="html.parser")
    table = bs.find("table", attrs={"summary": "forum_88"})
    tbodys = table.find_all("tbody", id=re.compile("^normalthread"))
    for t in tbodys:
        th = t.find("th", class_="common")
        # th = t.find("label", string=re.compile(".*爱家.*"))
        if th is not None:
            a = th.find("a")
            if a is not None:
                title = a.text
                href = a['href']

                b = re.match(".*爱家.*", title)
                c = re.match(".*尚城.*", title)
                if b or c:
                    print(title, href)


if __name__ == "__main__":
    start()