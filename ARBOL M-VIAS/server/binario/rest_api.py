from flask import Flask, jsonify, request
from flask_cors import CORS
from binary_search_tree import BinarySearchTree as BST

app = Flask(__name__)
CORS(app)

tree = BST()


@app.route('/get_tree', methods=['GET'])
def index():
    return jsonify(tree.level_order_traversal()), 200


@app.route('/insert_node', methods=['POST'])
def insert():
    try:
        data = request.get_json()
        nodo = data['nodo']
        if tree.search(float(nodo)) is not None:
            return jsonify({'error': 'El nodo ya existe'}), 400
        tree.insert(float(nodo))
        return jsonify({'mensaje': 'Insertado con exito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/delete_node', methods=['POST'])
def delete():
    try:
        data = request.get_json()
        nodo = data['nodo']
        if tree.search(float(nodo)) is None:
            return jsonify({'error': 'El nodo no existe'}), 400
        tree.delete(float(nodo))
        return jsonify({'mensaje': 'Eliminado con exito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/vaciar', methods=['GET'])
def vaciar():
    tree.clear()
    return jsonify({'mensaje': 'Arbol vaciado con exito'}), 200


if __name__ == '__main__':
    app.run(debug=True)