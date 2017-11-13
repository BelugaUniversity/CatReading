from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    return 'Hello index!'


@app.route('/hello/<int:user_name>')
def hello(user_name):
    return 'hello' + str(user_name)


if __name__ == '__main__':
    # 启动调试模式
    app.debug = True
    app.run()
