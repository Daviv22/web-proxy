from flask import Flask, send_from_directory
import os
import requests
from utils import write_log, get_data, check_url, get_json_blocked, get_domain

app = Flask(__name__)

blocked = get_json_blocked()

@app.route('/')
def hello_world():
    lista = []
    for site in blocked["blocked"]:
        lista.append(f'<p>{site}</p>')
    return "".join(lista)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/<path:url>')
def pegar_url(url):
    url = check_url(url)
    domain = get_domain(url)
    if domain in blocked["blocked"]:
        write_log(get_data(), get_domain(url), "blocked")
        return f'<p>Site banido</p>'
    else:
        r = requests.get(url)
        write_log(get_data(), get_domain(url), "allowed")
        return r.text

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
