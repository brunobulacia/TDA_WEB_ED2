from flask import Flask, jsonify, request
from flask_cors import CORS
from arbol_mvias import ArbolMVias

app = Flask(__name__)
CORS(app)

tree = ArbolMVias(2)
tree.insertar_dato(150)
tree.insertar_dato(300)
tree.insertar_dato(400)
tree.insertar_dato(100)
tree.insertar_dato(110)
# tree.insertar_dato(110)
# tree.insertar_dato(180)
# tree.insertar_dato(210)
# tree.insertar_dato(200)
# tree.insertar_dato(190)

@app.route('/get_tree', methods=['GET'])
def index():
    # print(tree.get_diccionario())
    return jsonify(tree.recorrido_por_niveles()), 200

@app.route('/get_raiz', methods=['GET'])
def get_raiz():
    print(tree.get_raiz())
    return jsonify('raiz'), 200



@app.route('/insertar_dato', methods=['POST'])
def insert():
    try:
        data = request.get_json()
        dato = data['dato']
        tree.insertar_dato(dato)
        return jsonify({'mensaje': 'Insertado con exito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/eliminar_dato', methods=['POST'])  
def delete():
    try:
        data = request.get_json()
        dato = data['dato']
        tree.eliminar_dato(dato)
        return jsonify({'mensaje': 'Eliminado con exito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)