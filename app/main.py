from flask import Flask, jsonify, request

app = Flask(__name__)

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/add", methods=["GET"])
def add_route():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"result": add(a, b)}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
