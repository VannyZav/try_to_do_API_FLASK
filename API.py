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


@app.route("/create/", methods=["POST"])
def create():
    new_twit = Twit(**request.json)
    strg_twit = next((twit for twit in storage if twit['_id'] == new_twit._id), None)
    # strg_twit = next((twit for twit in storage if new_twit._id in twit), None)
    if strg_twit:
        return f'twit with such id already created'
    else:
        storage.append(new_twit)
        return jsonify(new_twit), 201
    # id = request.args.get("id")
    # data = request.get_json()
    # twit = Twit(data["id"], data["body"], data["author"])
    # storage.append(twit)
    # return jsonify(twit), 201
  # data = request.get_json()
  #   req_twit = Twit(data["id"], data["body"], data["author"])
# next((twit for twit in storage if twit["id"] == req_twit.id), None)




@app.route("/twits/<_id>/")
def get_twit(_id):
    twit = next((twit for twit in storage if twit["_id"] == str(_id)), None)
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
        if not str(_id) in dict_["_id"]:
            return "haven't such id"
        elif dict_["_id"] == _id:
            storage[storage.index(dict_)] = twit
            dict_["_id"] = _id
            return jsonify(storage)


@app.route("/<_id>", methods=["DELETE"])
def delete(_id):
    for dict_ in storage:
        if _id == dict_['_id']:
            del storage[storage.index(dict_)]
            return '200'


if __name__ == "__main__":
    app.run(debug=True)