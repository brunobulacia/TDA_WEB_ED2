
from flask import Flask, jsonify, request
from flask_cors import CORS
from grafoPesado import Grafo, Vertice

# Crear el grafo
grafo = Grafo()
# Agregar vértices
for vertice_id in ['A', 'E', 'C', 'D', 'B']:
    grafo.add_vertice(Vertice(vertice_id))

# Agregar aristas con pesos
grafo.add_arista('A', 'B', 1)
grafo.add_arista('A', 'C', 4)
grafo.add_arista('B', 'C', 2)
grafo.add_arista('B', 'D', 5)
grafo.add_arista('C', 'D', 1)
grafo.add_arista('D', 'E', 3)


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


@app.route('/dijkstra', methods=['POST'])
def dijkstra():
    try:
        data = request.get_json()
        v1 = data['v1']
        v2 = data['v2']
        ruta, distancia = grafo.dijkstra(v1, v2)
        return jsonify({'ruta': ruta, 'distancia': distancia}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/bfs', methods=['POST'])
def bfs():
    try:
        data = request.get_json()
        v = data['v']
        bfs = grafo.bfs(v)
        return jsonify({'bfs': bfs}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/dfs', methods=['POST'])
def dfs():
    try:
        data = request.get_json()
        v = data['v']
        dfs = grafo.dfs(v)
        return jsonify({'dfs': dfs}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
