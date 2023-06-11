from flask import Flask, jsonify, request, render_template

import json

app = Flask(__name__)
data_file = 'data.json'

# Read the JSON file
def read_data():
    with open(data_file, 'r') as file:
        data = json.load(file)
    return data

# Write the JSON file
def write_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

# Index
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    data = read_data()
    return jsonify(data)

# Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    data = read_data()
    new_item = request.get_json()

    # Generate a unique ID for the new item
    new_item_id = len(data) + 1
    new_item['id'] = new_item_id

    if not isinstance(data, list):
        data = [data]

    data.append(new_item)
    write_data(data)  # Write the updated data to the file

    return jsonify(new_item), 201

# Update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = read_data()
    for item in data:
        if item['id'] == item_id:
            updated_item = request.get_json()
            item.update(updated_item)
            write_data(data)
            return jsonify(updated_item)
    return jsonify({'message': 'Item not found'}), 404

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    data = read_data()
    for item in data:
        if item['id'] == item_id:
            data.remove(item)
            write_data(data)
            return jsonify({'message': 'Item deleted'})
    return jsonify({'message': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
