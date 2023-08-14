import asyncio
import requests
import re
import json
from tikhub import DouyinAPI


#https://github.com/TikHubIO/Douyin-TikTok-API-Python-SDK
domain = 'https://api.tikhub.io'
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Ijc1NDExOTQ5M0BxcS5jb20iLCJleHAiOjE3MjM1MTUzNzEsImVtYWlsIjoiNzU0MTE5NDkzQHFxLmNvbSIsImV2aWwxIjoiJDJiJDEyJHNlMnM0cFZueTFTc0VVdWdSeW5wS2UyellXSWFqVUZnck16eS9VL0F1ZktOMXRYYWN6aWNpIn0.yIE5-GVH6DCgAbwIg0Rg_OEpnLL4vVVfUNfvCKTv2bM"
headers = {
    'Authorization':
    f'Bearer {token}',
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}


#用户信息
def getUserInfo():
    url = f'{domain}/users/me/'
    req = requests.get(url, headers=headers)
    printJson(req.text)


#签到
def checkIn():
    url = f'{domain}/promotion/daily_check_in'
    req = requests.get(url, headers=headers)
    print(req.text)


#json美化打印
def printJson(jsonStr):
    print(json.dumps(json.loads(jsonStr), indent=4, sort_keys=True))


async def get_douyin_video_data(douyin_video_url: str = None,
                                video_id: int = None,
                                language: str = 'zh') -> dict:

    endpoint = "/douyin/video_data/"
    video_id = None
    params = f'video_id={video_id}&language={language}'
    url = f'{domain}{endpoint}?{params}'
    result = requests.get(url, headers)
    return result.text



if __name__ == "__main__":
    # checkIn()
    getUserInfo()