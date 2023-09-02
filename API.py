from flask import Flask, request, jsonify
from flask.json.provider import DefaultJSONProvider

from storage import storage
from twit import Twit

app = Flask(__name__)


class CustomJSONProvider(DefaultJSONProvider):
    @staticmethod
    def default(obj):
        if isinstance(obj, Twit):
            return {'id': obj.id, 'body': obj.body, 'author': obj.author}
        else:
            return DefaultJSONProvider.default(obj)


app.json = CustomJSONProvider(app)


@app.route("/", methods=["POST"])
def create():
    data = request.get_json()
    twit = Twit(data["id"], data["body"], data["author"])
    for dict_ in storage:
        if twit not in dict_:
            storage.append(twit)
            return jsonify(twit), 201


@app.route("/", methods=["GET"])
def read():
    return jsonify(storage)


@app.route("/<_id>", methods=["PUT"])
def update(_id):
    data = request.get_json()
    twit = Twit(_id, data["body"], data["author"])
    for dict_ in storage:
        if not str(_id) in dict_["id"]:
            return "haven't such id"
        elif dict_["id"] == _id:
            storage[storage.index(dict_)] = twit
            dict_["id"] = _id
            return jsonify(storage)

@app.route("/<_id>", methods=["DELETE"])
def delete(_id):
    for dict_ in storage:
        if _id == dict_['id']:
            del storage[storage.index(dict_)]
            return '200'


if __name__ == "__main__":
    app.run(debug=True)
