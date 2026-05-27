from flask import Flask
import json

app = Flask(__name__)

blocked = json.loads(open('blocked.json').read())

@app.route('/')
def hello_world():
    lista = []
    for site in blocked["blocked"]:
        lista.append(f'<p>{site}</p>')
    return "".join(lista)

@app.route('/<url>')
def pegar_url(url):
    if url in blocked["blocked"]:
        return f'<p>Site banido</p>'
    else:
        return f"<p>{url}</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
