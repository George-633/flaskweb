from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm


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

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('username:{}, remember me:{}'.format(
            form.username.data, form.remember_me.data)
        )
        return redirect('./index')
    return render_template('login.html', title='login', form=form)