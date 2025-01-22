from flask import Flask
import webbrowser
import logging

# Configuration du logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Test de serveur Flask</h1>'

if __name__ == '__main__':
    try:
        # Configuration du serveur
        port = 5000
        url = f"http://127.0.0.1:{port}"
        
        # Ouvrir le navigateur automatiquement
        webbrowser.open_new(url)
        
        # Démarrer le serveur
        logger.info(f"Démarrage du serveur sur {url}")
        app.run(
            host='127.0.0.1',
            port=port,
            debug=False,
            use_reloader=False
        )
    except Exception as e:
        logger.error(f"Erreur: {str(e)}")
        raise
