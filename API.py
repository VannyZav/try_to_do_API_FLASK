from flask import Flask, request, jsonify
from flask.json.provider import DefaultJSONProvider

from storage import storage
from twit import Twit


app = Flask(__name__)


class CustomJSONProvider(DefaultJSONProvider):
    @staticmethod
    def default(obj):
        if isinstance(obj, Twit):
            return {'body': obj.body, 'author': obj.author}
        else:
            return DefaultJSONProvider.default(obj)


app.json = CustomJSONProvider(app)


@app.route("/", methods=["POST"])
def create():
    data = request.get_json()
    twit = Twit(data["body"], data["author"])
    storage.append(twit)
    return jsonify(twit), 201


@app.route("/", methods=["GET"])
def read():
    return jsonify(storage)


if __name__ == "__main__":
    app.run(debug=True)



