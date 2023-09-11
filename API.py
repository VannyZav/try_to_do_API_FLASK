from flask import Flask, request, jsonify

app = Flask(__name__)

storage = [{
    "id": 1,
    "body": "texttexttext",
    "author": "somebody"
}]


@app.route("/create/", methods=["POST"])
def create():
    new_twit = request.get_json()

    _id = len(storage) + 1

    twit = {"id": _id,
            "body": new_twit["body"],
            "author": new_twit["author"]
            }
    storage.append(twit)
    return jsonify(twit)


@app.route("/read/<int:_id>/")
def get_twit(_id):
    for twit in storage:
        if twit["id"] == _id:
            return jsonify(twit)
    return jsonify({"status: "f"Twit with id {_id} not found"})


@app.route("/read/")
def get_twits():
    return jsonify(storage)


@app.route("/update/<int:_id>/", methods=["PUT"])
def update(_id):
    data = request.get_json()
    for twit in storage:
        if twit["id"] == _id:
            twit["body"] = data["body"]
            twit["author"] = data["author"]
            return jsonify({"status": "twit updated successfully"})
    return jsonify({"status": f"twit with id {_id} not found"})


@app.route("/delete/<int:_id>/", methods=["DELETE"])
def delete(_id):
    for twit in storage:
        if twit["id"] == _id:
            storage.remove(twit)
            return jsonify({"status": "twit deleted successfully"})
    return jsonify({"status": f"twit with id {_id} not found"})


if __name__ == "__main__":
    app.run()
