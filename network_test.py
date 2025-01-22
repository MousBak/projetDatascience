import socket
import logging
import subprocess
import sys
import os
from flask import Flask

# Configuration du logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def check_network():
    logger.info("=== Test de la configuration réseau ===")
    
    # 1. Vérifier l'interface loopback
    try:
        logger.info("Test de l'interface loopback...")
        socket.gethostbyname('localhost')
        logger.info("✓ Interface loopback OK")
    except Exception as e:
        logger.error(f"✗ Problème avec l'interface loopback: {e}")
        
    # 2. Vérifier les ports utilisés
    try:
        logger.info("\nPorts actuellement utilisés:")
        if os.name == 'nt':  # Windows
            netstat = subprocess.check_output('netstat -an', shell=True).decode()
            for line in netstat.split('\n'):
                if 'LISTENING' in line:
                    logger.info(line.strip())
    except Exception as e:
        logger.error(f"Erreur lors de la vérification des ports: {e}")
    
    # 3. Test de bind sur différents ports
    test_ports = [3000, 5000, 8050, 8080]
    available_ports = []
    
    logger.info("\nTest des ports disponibles:")
    for port in test_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind(('127.0.0.1', port))
            available_ports.append(port)
            logger.info(f"✓ Port {port} disponible")
        except Exception as e:
            logger.error(f"✗ Port {port} non disponible: {e}")
        finally:
            sock.close()
            
    return available_ports

# Créer une application Flask minimale
app = Flask(__name__)

@app.route('/')
def home():
    return 'Test de serveur - Si vous voyez ce message, le serveur fonctionne!'

if __name__ == '__main__':
    logger.info("\n=== Démarrage des tests réseau ===\n")
    
    # Vérifier la configuration réseau
    available_ports = check_network()
    
    if not available_ports:
        logger.error("Aucun port disponible trouvé!")
        sys.exit(1)
        
    # Utiliser le premier port disponible
    port = available_ports[0]
    
    logger.info(f"\n=== Tentative de démarrage du serveur sur le port {port} ===")
    logger.info(f"Essayez d'accéder à:")
    logger.info(f"1. http://localhost:{port}")
    logger.info(f"2. http://127.0.0.1:{port}")
    
    try:
        app.run(
            host='127.0.0.1',
            port=port,
            debug=True
        )
    except Exception as e:
        logger.error(f"Erreur lors du démarrage du serveur: {e}")
        raise
