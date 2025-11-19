from flask import Flask, jsonify

app = Flask(__name__)

USERS = [
    {"id": 1, "name": "Alice", "status": "active"},
    {"id": 2, "name": "Bob", "status": "inactive"},
    {"id": 3, "name": "Charlie", "status": "active"},
]

@app.route('/users')
def get_users():
    return jsonify(USERS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
