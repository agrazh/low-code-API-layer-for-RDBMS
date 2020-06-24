from flask import Flask, jsonify, request

stores = [{
    'name': 'Store One',
    'items': [{'name':'Paper A4', 'price': 0.99 }]
}]

app = Flask(__name__)

# Endpoints with GET, POST methods
# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'not found'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
                new_item = {
                    'name': request_data['name'],
                    'price': request_data['price']
                }
                store['items'].append(new_item)
                return jsonify(store)
    return jsonify({'message': 'not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_itme_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'not found'})

app.run(port=4000)
