import json
import re
from datetime import datetime
from urllib.parse import urlparse

def get_json_blocked():
    with open("blocked.json", "r") as f:
        blocked = json.load(f)
    return blocked

def get_json_log():
    with open("log.json", "r") as f:
        log = json.load(f)
    return log

def get_json_words():
    with open("words.json", "r") as f:
        words = json.load(f)
    return words

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

def check_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
        return url
    else:
        return url

def get_domain(url):
    parsed_url = urlparse(url)
    return f"{parsed_url.netloc}"

def filter_content(content):
    words = get_json_words()

    filtered_content = content

    for palavrao, substituto in words.items():
        padrao = re.compile(rf'\b{palavrao}\b', re.IGNORECASE)
        filtered_content = padrao.sub(substituto, filtered_content)

    return filtered_content
