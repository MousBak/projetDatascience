import dash
from dash import html
import dash_bootstrap_components as dbc
import logging

# Configuration du logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialisation de l'application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout simple
app.layout = html.Div([
    html.H1("Test de connexion"),
    html.P("Si vous voyez cette page, le serveur fonctionne correctement!")
])

if __name__ == '__main__':
    try:
        port = 9999  # Un port moins susceptible d'être utilisé
        host = '127.0.0.1'
        
        logger.info(f"=== Démarrage du serveur sur {host}:{port} ===")
        logger.info(f"Accédez à : http://{host}:{port}")
        
        app.run_server(
            host=host,
            port=port,
            debug=True,
            dev_tools_hot_reload=False  # Désactiver le hot reload pour éviter les conflits
        )
    except Exception as e:
        logger.error(f"Erreur lors du démarrage du serveur: {str(e)}")
        raise
