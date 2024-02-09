from flask import Flask, request, jsonify
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
# Restful API: GET, POST, PUT, DELETE
@app.route('/test_get', methods=['GET'])
def test_get():
    return jsonify({'message': 'Hello, World!'})

@app.route('/test_post', methods=['POST'])
def test_post():
    data = request.get_json()
    print(data)
    return jsonify({'message': 'Hello, ' + data['name']})



if __name__ == '__main__':
    app.run(debug=True)