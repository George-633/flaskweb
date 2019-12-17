from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'duke'}
    posts = [
        {
            'author': {'username': '刘'},
            'body': '这是模板模块中的循环例子～1'

        },
        {
            'author': {'username': '忠强'},
            'body': '这是模板模块中的循环例子～2'
        }
    ]
    return render_template('index.html', title='My', user=user, posts=posts)