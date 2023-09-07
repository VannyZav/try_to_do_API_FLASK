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


@app.route("/create/", methods=["POST"])
def create():
    data = request.get_json()
    id = request.args.get("id")
    req_twit = Twit(data["id"], data["body"], data["author"])
    strg_twit = next((twit for twit in storage if twit["id"] == id), None)
    if strg_twit:
        return f'twit with such id already created'

    storage.append(req_twit)
    return jsonify(req_twit), 201
    # id = request.args.get("id")
    # data = request.get_json()
    # twit = Twit(data["id"], data["body"], data["author"])
    # storage.append(twit)
    # return jsonify(twit), 201


@app.route("/twits/<_id>/")
def get_twit(_id):
    twit = next((twit for twit in storage if twit["id"] == str(_id)), None)
    if twit:
        return jsonify(twit)
    else:
        return f"Twit with id {_id} not found"


@app.route("/twits/")
def get_twits():
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