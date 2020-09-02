from flask import Flask, abort, request, jsonify
from flask_cors import CORS
from datetime import timedelta, datetime
from random import randint

app = Flask(__name__)
CORS(app)
res = [1, 2, 3]


@app.route('/get_second/<value>', methods=['GET'])
def get_second(value):
    return jsonify(res)


@app.route('/get_third/<value>', methods=['GET'])
def get_third(value):
    return jsonify(res)


@app.route('/get_chart', methods=['GET'])
def get_chart():
    res = []
    start = datetime(2019, 9, 1, 0, 0, 0)
    interval = timedelta(minutes=30)
    for i in range(300):
        res.append({'x': start.strftime('%Y-%m-%d %H:%M:%S'), 'y': randint(10, 50)})
        start = start + interval
    return jsonify(res)


@app.route('/upload', methods=['POST'])
def upload():
    print(request.form)
    avatar = request.files.get('img')
    if avatar:
        avatar.save(avatar.filename)

    return jsonify(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8086, debug=True)
