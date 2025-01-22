from flask import Flask, render_template_string
import webbrowser
from threading import Timer

app = Flask(__name__)

# Template HTML simple
template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Test Application</title>
    <style>
        body { 
            font-family: Arial, sans-serif;
            margin: 40px;
            text-align: center;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        h1 { color: #333; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Test Application</h1>
        <p>Si vous voyez cette page, le serveur fonctionne correctement!</p>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(template)

def open_browser():
    webbrowser.open_new('http://localhost:3000/')

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(host='localhost', port=3000, debug=False)
