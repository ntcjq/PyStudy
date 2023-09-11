from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import json
from flask import Blueprint  # 导入蓝图模块

# Blueprint两个参数（'蓝图名字',蓝图所在位置')
test_blue = Blueprint('test', __name__)


@test_blue.route("/user/list")
def userList():
    return ["cjq", "ssn", "hyh"]


@test_blue.route("/username/<username>")
def username(username):
    return f'Hello {username}'


@test_blue.route("/userId/<int:userId>")
def userId(userId):
    return f'Hello {userId}'


@test_blue.route('/template')
def template():
    int_ = 1024
    str_ = 'Hello World!'
    list_ = [1, 2, 3, 4, 5]
    dict_ = {'name': 'Kint', 'age': 23}
    # render_template方法:渲染模板
    # 参数1: 模板名称  参数n: 传到模板里的数据
    return render_template('test/template.html',
                           my_int=int_,
                           my_str=str_,
                           my_list=list_,
                           my_dict=dict_)
