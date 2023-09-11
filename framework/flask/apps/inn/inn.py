from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import json
from flask import Blueprint  # 导入蓝图模块

# Blueprint两个参数（'蓝图名字',蓝图所在位置')
inn_blue = Blueprint('inn', __name__)


@inn_blue.route('/ui')
def ui():
    return render_template('inn/ui.html')


@inn_blue.route('/register')
def register():
    result = {}
    result['x'] = [
        '2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04', '2023-07-05'
    ]
    result['y'] = [10, 20, 30, 35, 36]
    return json.dumps(result)
