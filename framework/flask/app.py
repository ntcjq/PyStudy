from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import json
from apps.inn.inn import inn_blue
from apps.test.test import test_blue

# 创建应用实例
app = Flask(__name__, template_folder='templates', static_folder='static')

#将蓝图注册到app中
app.register_blueprint(inn_blue)
app.register_blueprint(test_blue)


# 视图函数（路由）
@app.route("/", methods=['GET'])
def hello_world():
    return "Hello, World!"


# 启动服务
if __name__ == '__main__':
    app.run(debug=True)
