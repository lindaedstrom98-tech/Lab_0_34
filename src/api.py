from flask import Flask, request, jsonify
from calculator import Calculator

app = Flask(__name__)
calculator = Calculator()

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello World!"})

@app.route("/calc", methods=["POST"])
def calc():
    data = request.get_json()
    expression = data["expression"]

    result = calculator.calc(expression)

    return jsonify({
        "expression": expression,
        "result": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)