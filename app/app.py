from urllib import request

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    requesturl = request.url
    return jsonify({
        "endpoints": "add, sub, div, mul",
        "params": "num1, num2",
        "example": requesturl + "div?num1=1234&num2=2344"
    })


def parse_params():
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        return [num1, num2]
    except ValueError as e:
        return []


@app.route("/add")
def add():
    nums = parse_params()

    if len(nums) == 0:
        return jsonify({
            "error": "invalid parameters"
        })

    return jsonify({
        "result": nums[0] + nums[1]
    })


@app.route("/sub")
def sub():
    nums = parse_params()

    if len(nums) == 0:
        return jsonify({
            "error": "invalid parameters"
        })

    return jsonify({
        "result": nums[0] - nums[1]
    })


@app.route("/div")
def div():
    nums = parse_params()

    if len(nums) == 0:
        return jsonify({
            "error": "invalid parameters"
        })

    return jsonify({
        "result": nums[0] / nums[1]
    })


@app.route("/mul")
def mul():
    nums = parse_params()

    if len(nums) == 0:
        return jsonify({
            "error": "invalid parameters"
        })

    return jsonify({
        "result": nums[0] * nums[1]
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
