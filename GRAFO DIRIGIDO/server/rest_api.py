
from flask import Flask, jsonify, request
from flask_cors import CORS
from grafoPesado import Grafo, Vertice

grafo = Grafo()


app = Flask(__name__)
CORS(app) 

@app.route('/vaciar', methods=['POST'])
def reiniciar():
    try:
        grafo.clear()
        return jsonify({'message': 'Grafo vaciado'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_grafo', methods=['GET'])
def get_grafo():
    return jsonify(grafo.get_grafo()), 200

@app.route('/get_vertices', methods=['GET'])
def get_vertices():
    return jsonify(grafo.get_vertices()), 200

@app.route('/add_arista', methods=['POST'])
def add_arista():
    try:
        data = request.get_json()
        v1 = data['v1']
        v2 = data['v2']
        peso = data['peso']
        grafo.add_arista(v1, v2, peso)
        return jsonify({'message': 'Arista agregada'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/add_vertice', methods=['POST'])
def add_vertice():
    try:
        print('hola')
        data = request.get_json()
        v = data['v']
        grafo.add_vertice(Vertice(v))
        return jsonify({'message': 'Vertice agregado'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/remove_arista', methods=['POST'])
def remove_arista():
    try:
        data = request.get_json()
        v1 = data['v1']
        v2 = data['v2']
        grafo.remove_arista(v1, v2)
        return jsonify({'message': 'Arista eliminada'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/remove_vertice', methods=['POST'])
def remove_vertice():
    try:
        data = request.get_json()
        v = data['v']
        grafo.remove_vertice(v)
        return jsonify({'message': 'Vertice eliminado'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
