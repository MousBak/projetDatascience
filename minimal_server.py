from flask import Flask
import socket
import logging

# Configuration du logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Test de Connexion</h1>'

def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(('0.0.0.0', port))
        sock.close()
        return True
    except:
        return False

def find_available_port():
    for port in [3000, 5000, 8050, 8080]:
        if check_port(port):
            return port
    return None

if __name__ == '__main__':
    try:
        # Trouver un port disponible
        port = find_available_port()
        if port is None:
            logger.error("Aucun port disponible trouvé")
            exit(1)
            
        # Configuration du serveur
        host = '0.0.0.0'  # Écoute sur toutes les interfaces
        
        logger.info(f"Tentative de démarrage du serveur sur {host}:{port}")
        logger.info(f"Vous pourrez accéder au serveur via:")
        logger.info(f"- http://localhost:{port}")
        logger.info(f"- http://127.0.0.1:{port}")
        
        # Démarrer le serveur
        app.run(
            host=host,
            port=port,
            debug=True
        )
    except Exception as e:
        logger.error(f"Erreur lors du démarrage du serveur: {str(e)}")
        raise
