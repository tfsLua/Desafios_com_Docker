from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Hello from Server! Current time: {now}\n"

if __name__ == '__main__':
    # O servidor roda na porta 8080 conforme o requisito
    app.run(host='0.0.0.0', port=8080)
