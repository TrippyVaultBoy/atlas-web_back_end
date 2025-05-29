from flask import Flask, jsonify, request


app = Flask(__name__)


items = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"},
    ]


@app.route('/')
def home():
    return "Welcome to a basic Flask API"


@app.route('/api/items', methods=['GET'], strict_slashes=False)
def get_items():
    return jsonify(items)


@app.route('/api/items/<int:item_id>', methods=['GET'], strict_slashes=False)
def get_item(item_id):
    for item in items:
        if item['id'] == item_id:
            item = item_id
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    else:
        return jsonify(item)


@app.route('/api/items', methods=['POST'], strict_slashes=False)
def add_item():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Bad request"}), 400
    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,
        "name" : data['name']
    }
    items.append(new_item)
    return jsonify(new_item), 201


@app.route('/api/items/<int:item_id>', methods=['DELETE'], strict_slashes=False)
def delete_item(item_id):
    for item in items:
        if item['id'] == item_id:
            item = item_id
    if item is None:
        return jsonify({"error": "Bad request"})
    else:
        del item
        return True


if __name__ == '__main__':
    app.run(debug=True, port=8080)