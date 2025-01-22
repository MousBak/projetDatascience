from flask import Flask
import socket
import logging
import os
import sys
import colorama
from colorama import Fore, Style

# Initialiser colorama pour les couleurs dans le terminal Windows
colorama.init()

# Configuration du logging avec des couleurs
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)
logger = logging.getLogger(__name__)

def print_header(text):
    print(f"\n{Fore.CYAN}{'='*20} {text} {'='*20}{Style.RESET_ALL}")

def print_success(text):
    print(f"{Fore.GREEN}[OK] {text}{Style.RESET_ALL}")

def print_error(text):
    print(f"{Fore.RED}[ERROR] {text}{Style.RESET_ALL}")

def print_info(text):
    print(f"{Fore.YELLOW}[INFO] {text}{Style.RESET_ALL}")

def check_server():
    print_header("VERIFICATION DU SERVEUR")
    
    # 1. Vérifier localhost
    print_info("\n1. Test de localhost...")
    try:
        ip = socket.gethostbyname('localhost')
        print_success(f"localhost est configure correctement ({ip})")
    except Exception as e:
        print_error(f"Probleme avec localhost: {e}")
    
    # 2. Vérifier les ports
    print_info("\n2. Test des ports...")
    test_ports = [3000, 5000, 8050, 8080]
    available_ports = []
    
    for port in test_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind(('127.0.0.1', port))
            available_ports.append(port)
            print_success(f"Port {port} est disponible")
        except Exception as e:
            print_error(f"Port {port} n'est pas disponible")
        finally:
            sock.close()
    
    # 3. Tester une connexion simple
    if available_ports:
        port = available_ports[0]
        print_info(f"\n3. Tentative de demarrage d'un serveur test sur le port {port}...")
        
        app = Flask(__name__)
        
        @app.route('/')
        def home():
            return 'Test Serveur OK'
        
        print_info(f"Le serveur va demarrer sur: http://localhost:{port}")
        print_info("Vous devriez voir 'Test Serveur OK' dans votre navigateur")
        print_info("Appuyez sur Ctrl+C pour arreter le serveur")
        
        try:
            app.run(host='127.0.0.1', port=port)
        except Exception as e:
            print_error(f"Erreur lors du demarrage du serveur: {e}")
    else:
        print_error("Aucun port disponible trouve!")

if __name__ == '__main__':
    try:
        check_server()
    except KeyboardInterrupt:
        print_info("\nServeur arrete par l'utilisateur")
    except Exception as e:
        print_error(f"Erreur inattendue: {e}")
