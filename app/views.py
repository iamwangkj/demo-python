from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Wangkj' } # fake user
    return render_template(
        "index.html",
        title = 'Home',
        user = user
    )


@app.route('/users')
def users():
    return "users1"