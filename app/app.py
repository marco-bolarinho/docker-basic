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
    except ValueError as _:
        return []


def process(operation: str) -> jsonify:
    nums = parse_params()

    if len(nums) == 0:
        return jsonify({
            "error": "invalid parameters"
        })

    result = 0
    match operation:
        case "+": result = nums[0] + nums[1]
        case "-": result = nums[0] - nums[1]
        case "*": result = nums[0] * nums[1]
        case "/": result = nums[0] / nums[1]

    return jsonify({
        "result": result,
    })


@app.route("/add")
def add():
    return process("+")


@app.route("/sub")
def sub():
    return process("-")


@app.route("/div")
def div():
    return process("/")


@app.route("/mul")
def mul():
    return process("*")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
