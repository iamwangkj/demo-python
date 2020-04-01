from app import app, mongo
from flask import render_template, jsonify, make_response
import json


@app.route('/')
@app.route('/index')
def index():
    users_online = mongo.db.users.find({'online': True})
    print(type(users_online))
    res = []
    for item in users_online:
        res.append(item)
    print(res)

    print(type(res))
    return jsonify({'data': res})


@app.route('/users')
def getUsers():
    res = mongo.db.users.insert({
        'name': 'wangkj',
        'online': True
    })
    return res


@app.route('/users', methods=['POST'])
def addUsers():
    return "users1"
