from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])  
def index():
    return jsonify({'lista': [1,2,4 ]})

if __name__ == '__main__':
    app.run(debug=True)