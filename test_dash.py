import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1("Test de connexion"),
    html.P("Si vous voyez cette page, le serveur fonctionne correctement!")
])

if __name__ == '__main__':
    print("=== Démarrage du serveur ===")
    print("Accédez à : http://127.0.0.1:5000")
    app.run_server(host='127.0.0.1', port=5000, debug=True)
