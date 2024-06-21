from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import json
from apps.user.user import user_blue
import webview

# 创建应用实例
app = Flask(__name__, template_folder='templates', static_folder='static')

#将蓝图注册到app中
app.register_blueprint(user_blue)

# 视图函数（路由）
@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.before_request
def before_request_a():
    print('I am in before_request_a')
 
@app.before_request
def before_request_b():
    print('I am in before_request_b')

@app.after_request
def after_request_a(response):
    print('I am in after_request_a')
    # 该装饰器接收response参数，运行完必须归还response，不然程序报错
    return response


# 启动服务
if __name__ == '__main__':
    # 直接启动
    app.run(debug=True)

    # window = webview.create_window(
    #     title='用户管理',
    #     width=1920,
    #     height=820,
    #     url=app,		# 这里直接将实例化后的flask对象传给url参数就可以自动启动web服务了
    #     confirm_close=True		# 退出时提示
    # )
    # # 自定义退出提示的中文内容
    # cn = {
    #     'global.quitConfirmation': u'确定关闭?'
    # }
    # webview.start(localization=cn, gui='mshtml')
