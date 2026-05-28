import json
from datetime import datetime
import tldextract

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

def get_data():
    data = datetime.now()
    data = f"{data.year}-{data.month}-{data.day} {data.hour}:{data.minute}:{data.second}"
    return data

def get_domain(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    domain = tldextract.extract(url)
    return f"{domain.domain}.{domain.suffix}"