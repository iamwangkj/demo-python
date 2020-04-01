from app import app, mongo
from flask import render_template, jsonify, make_response


@app.route('/')
@app.route('/index')
def index():
    arr = mongo.db.users.find({'online': True})
    res = []
    for item in arr:
        _id = item.pop("_id")
        item["id"] = str(_id)
        res.append(item)
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
