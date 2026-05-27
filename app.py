from flask import Flask
import json
from datetime import datetime

app = Flask(__name__)

blocked = json.loads(open('blocked.json').read())

def get_json_log():
    with open("log.json", "r") as f:
        log = json.load(f)
    return log

def write_log(timestamp, url, status):
    log = get_json_log()
    data_log = {
        "timestamp": timestamp,
        "url": url,
        "action": status
    }
    log.append(data_log)
    with open("log.json", "w") as f:
        json.dump(log, f, indent=3)

@app.route('/')
def hello_world():
    lista = []
    for site in blocked["blocked"]:
        lista.append(f'<p>{site}</p>')
    return "".join(lista)

@app.route('/<url>')
def pegar_url(url):
    if url in blocked["blocked"]:
        write_log(get_data(), url, "blocked")
        return f'<p>Site banido</p>'
    else:
        write_log(get_data(), url, "allowed")
        return f"<p>{url}</p>"

def get_data():
    data = datetime.now()
    data = f"{data.year}-{data.month}-{data.day} {data.hour}:{data.minute}:{data.second}"

    return data

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
