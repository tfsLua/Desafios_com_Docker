from flask import Flask, jsonify
import requests

app = Flask(__name__)

# O nome do host 'service_a' será resolvido pelo Docker Compose
SERVICE_A_URL = "http://service_a:5000/users"

@app.route('/combined_info')
def get_combined_info():
    try:
        response = requests.get(SERVICE_A_URL)
        response.raise_for_status()
        users = response.json()
        
        # Lógica de consumo e exibição combinada
        combined_data = [f"Usuário {user['name']} está {user['status']}" for user in users]
        
        return jsonify({"status": "success", "data": combined_data})
    except requests.exceptions.RequestException as e:
        return jsonify({"status": "error", "message": f"Erro ao comunicar com o Serviço A: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
