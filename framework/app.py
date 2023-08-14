from flask import Flask
# 创建应用实例
app = Flask(__name__)


# 视图函数（路由）
@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/user/list")
def userList():
    return ["cjq","ssn","hyh"]

@app.route("/username/<username>")
def username(username):
    return f'Hello {username}'

@app.route("/userId/<int:userId>")
def userId(userId):
    return f'Hello {userId}'


# 启动服务
if __name__ == '__main__':
    app.run(debug=True)
