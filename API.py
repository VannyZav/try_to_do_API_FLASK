from flask import Flask, request, jsonify
from flask.json.provider import DefaultJSONProvider

from storage import storage
from twit import Twit


app = Flask(__name__)


class CustomJSONProvider(DefaultJSONProvider):
    @staticmethod
    def default(obj):
        if isinstance(obj, Twit):
            return {'_id': obj._id, 'body': obj.body, 'author': obj.author}
        else:
            return DefaultJSONProvider.default(obj)


app.json = CustomJSONProvider(app)


@app.route("/", methods=["POST"])
def create():
    data = request.get_json()
    twit = Twit(data["_id"], data["body"], data["author"])
    storage.append(twit)
    return jsonify(twit), 201


@app.route("/", methods=["GET"])
def read():
    return jsonify(storage)


@app.route("/<_id>", methods=["PUT"])
def update(_id):
    ids = next((x for x in storage if x["_id"] == _id), None)
    data = request.get_json()
    if not ids:
        return {'message': 'No such id in storage'}
    ids.update(data)
    return ids


if __name__ != "__main__":
    app.run(debug=True)



