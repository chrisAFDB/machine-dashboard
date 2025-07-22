from flask import Flask, render_template

# Création de l'application Flask
app = Flask(__name__, template_folder='templates', static_folder='static')

# Route principale qui affiche le tableau de bord
@app.route('/')
def index():
    return render_template('index.html')

# Point d'entrée de l'application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
