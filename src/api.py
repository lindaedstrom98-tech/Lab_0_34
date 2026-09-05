from flask import Flask, jsonify

app = Flask(__name__)  #app är webbsidan och flask är ramverket som den använder


@app.route("/hello", methods=["GET"]) #Om någon skickar en GET-request till /hello, kör funktionen som kommer direkt under.
def hello():
    return jsonify({"message": "Hello World!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) #denna används för docker för flask måste lyssna på alla nätverksinterface och port 5000 är standardporten för flask.
