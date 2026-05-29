import json
import re
from datetime import datetime
from urllib.parse import urlparse



# Leitura de JSONs

def get_json_blocked():
    with open("blocked.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_json_log():
    with open("log.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_json_words():
    with open("words.json", "r", encoding="utf-8") as f:
        return json.load(f)



# Escrita de JSONs

def save_json_blocked(data):
    with open("blocked.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=3, ensure_ascii=False)

def save_json_words(data):
    with open("words.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=3, ensure_ascii=False)

def write_log(timestamp, url, status):
    log = get_json_log()
    data_log = {
        "timestamp": timestamp,
        "url": url,
        "action": status
    }
    log.append(data_log)
    with open("log.json", "w", encoding="utf-8") as f:
        json.dump(log, f, indent=3, ensure_ascii=False)



# Gerenciamento de sites

def write_blocked_site(site_id, url, timestamp):
    blocked = get_json_blocked()
    data_site = {
        "id": site_id,
        "url": url,
        "timestamp": timestamp,
    }
    blocked.append(data_site)
    save_json_blocked(blocked)

def edit_blocked_sites(site_id, new_url):
    blocked = get_json_blocked()
    for site in blocked:
        if site["id"] == site_id:
            site["url"] = new_url
            break
    save_json_blocked(blocked)

def delete_blocked_site_json(site_id):
    blocked = get_json_blocked()
    blocked = [s for s in blocked if s["id"] != site_id]
    save_json_blocked(blocked)



# Gerenciamento de palavrões

def write_swear_word(word_id, original, censored, timestamp):
    words = get_json_words()
    data_word = {
        "id": word_id,
        "original": original,
        "censored": censored,
        "added_at": timestamp,
    }
    words.append(data_word)
    save_json_words(words)

def edit_swear_word_json(word_id, original, censored):
    words = get_json_words()
    for word in words:
        if word["id"] == word_id:
            word["original"] = original
            word["censored"] = censored
            break
    save_json_words(words)

def delete_swear_word_json(word_id):
    words = get_json_words()
    words = [w for w in words if w["id"] != word_id]
    save_json_words(words)



# Funções auxiliares

def get_data():
    data = datetime.now()
    return data.strftime("%Y-%m-%d %H:%M:%S") # Jeito mais limpo de formatar data

def check_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        return "https://" + url
    return url

def get_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

def filter_content(content):
    words = get_json_words()
    filtered_content = content

    for item in words:
        palavrao = item["original"]
        substituto = item["censored"]
        padrao = re.compile(rf'\b{palavrao}\b', re.IGNORECASE)
        filtered_content = padrao.sub(substituto, filtered_content)

    return filtered_content
