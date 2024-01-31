from flask import Flask, request, jsonify
import json


app = Flask(__name__)

# Restful API: GET, POST, PUT, DELETE
@app.route('/test_get', methods=['GET'])
def api():
    return jsonify({'message': 'Hello, World!'})

@app.route('/test_post', methods=['POST'])
def api_post():
    data = request.get_json()
    print(data)
    return jsonify({'message': 'Hello, ' + data['name']})



if __name__ == '__main__':
    app.run(debug=True)