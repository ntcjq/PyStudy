import asyncio
import requests
import re
import json


def getDownloadUrl(share_url: str = None):
    headers = {
        'user-agent':
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36 Edg/103.0.1264.62'
    }
    #share_url = "https://v.douyin.com/iJPv8dAB/"
    req = requests.get(share_url, headers)
    #video_url = 'https://www.iesdouyin.com/share/video/7267008971532209463/?region=CN&mid=6873505795145730055&u_code=jm272f0k&did=MS4wLjABAAAAAx_JlfIughcT-Szlq0_eCDno4jTW0012oaf0F3f-CJHzv2IOHEdvNnjiyv-Vghks&iid=MS4wLjABAAAA5Kca_6QlwxS8Ix9mOkrrz2NspHSKjBdUzxm2OQFwBeHG2AerIfpZy-REOyG4M4Jp&with_sec_did=1&titleType=title&share_sign=QQgK1UIC.QuWGH2f8B1l4JGMYqDkMzh_x.WD7FBx4lA-&share_version=260400&ts=1691993348&from_ssr=1&timestamp=1691993416&utm_campaign=client_share&app=aweme&utm_medium=ios&tt_from=copy&utm_source=copy'
    video_url = req.url
    #video_id =  7267008971532209463
    video_id = re.findall('/video/(\d+)?', video_url)[0]
    print(video_id)
    # 提取带水印短视频链接地址
    # https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=7267008971532209463
    url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={video_id}'
    ree = requests.get(url, headers=headers)
    data = json.loads(ree.text)
    # 使用正则提取无水印视频链接
    result = data['item_list'][0]['video']['play_addr']['url_list'][0].replace(
        '/playwm/', '/play/')
    print("视频无水印url：" + result)


#下载
def download(video_url: str = None):
    response = requests.get(video_url)
    with open("file/video.mp4", "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    # checkIn()
    # getUserInfo()
    getDownloadUrl("https://v.douyin.com/iJPv8dAB/")