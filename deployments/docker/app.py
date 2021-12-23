from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_my_ip():
    return jsonify({
        'IP': request.remote_addr
        }), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
