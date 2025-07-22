from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder='template')

# Route principale (serve index.html)
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Route pour servir tous les fichiers statiques (HTML, CSS, JS)
@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory(app.static_folder, path)

# Exemple de route API
@app.route('/api')
def api_info():
    return jsonify({"message": "Machine Dashboard API"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
