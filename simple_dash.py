import dash
from dash import html
import dash_bootstrap_components as dbc
import logging
import webbrowser
from threading import Timer

# Configuration du logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def open_browser():
    webbrowser.open_new('http://localhost:8050/')

# Initialisation de l'application
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
)

# Layout simple
app.layout = dbc.Container([
    html.H1("Test Dashboard", className="text-center my-4"),
    html.P("Si vous voyez cette page, l'application fonctionne correctement!")
])

if __name__ == '__main__':
    try:
        logger.info("Démarrage de l'application...")
        Timer(1, open_browser).start()
        app.run_server(
            port=8050,
            host='localhost',
            debug=False,
            dev_tools_ui=False,
            dev_tools_props_check=False
        )
    except Exception as e:
        logger.error(f"Erreur lors du démarrage: {str(e)}")
        raise
