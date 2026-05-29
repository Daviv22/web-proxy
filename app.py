from flask import Flask, send_from_directory, render_template, request, redirect, url_for
import os
import uuid
import requests
from utils import (write_log, get_data, check_url, get_json_blocked, delete_blocked_site_json,
                   filter_content, get_json_words, write_blocked_site, edit_blocked_sites, write_swear_word,
                   edit_swear_word_json, delete_swear_word_json, get_domain, is_domain_blocked)

app = Flask(__name__)

swear_words = get_json_words()

@app.route('/')
def home():
    return render_template("home.html", active_page="home")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'vpn.png', mimetype='image/png')



# Sites bloqueados

@app.route("/blocked-sites")
def blocked_sites_page():
    return render_template(
        "blocked_sites.html",
        sites=get_json_blocked(),
        active_page="blocked_sites",
    )

@app.route("/blocked-sites/add", methods=["POST"])
def add_blocked_site():
    url = request.form.get("url", "").strip()
    if url:
        write_blocked_site(str(uuid.uuid4()), url, get_data())
    return redirect(url_for("blocked_sites_page"))


@app.route("/blocked-sites/edit/<site_id>", methods=["POST"])
def edit_blocked_site(site_id):
    new_url = request.form.get("url", "").strip()
    if new_url:
        edit_blocked_sites(site_id, new_url)
    return redirect(url_for("blocked_sites_page"))


@app.route("/blocked-sites/delete/<site_id>", methods=["POST"])
def delete_blocked_site(site_id):
    delete_blocked_site_json(site_id)
    return redirect(url_for("blocked_sites_page"))



# Palavrões

@app.route("/swear-words")
def swear_words_page():
    return render_template(
        "swear_words.html",
        words=get_json_words(),
        active_page="swear_words",
    )

@app.route("/swear-words/add", methods=["POST"])
def add_swear_word():
    original = request.form.get("original", "").strip()
    censored = request.form.get("censored", "").strip()
    if original and censored:
        write_swear_word(str(uuid.uuid4()), original, censored, get_data())
    return redirect(url_for("swear_words_page"))


@app.route("/swear-words/edit/<word_id>", methods=["POST"])
def edit_swear_word(word_id):
    original = request.form.get("original", "").strip()
    censored = request.form.get("censored", "").strip()
    if original and censored:
        edit_swear_word_json(word_id, original, censored)
    return redirect(url_for("swear_words_page"))


@app.route("/swear-words/delete/<word_id>", methods=["POST"])
def delete_swear_word(word_id):
    delete_swear_word_json(word_id)
    return redirect(url_for("swear_words_page"))



# Proxy

@app.route('/<path:url>')
def pegar_url(url):
    url = check_url(url)
    domain = get_domain(url)
    blocked_sites = [s["url"] for s in get_json_blocked()]
    if is_domain_blocked(domain, blocked_sites):
        write_log(get_data(), domain, "blocked")
        return render_template("forbidden.html")
    else:
        r = requests.get(url)
        filtered_content = filter_content(r.text)
        if filtered_content != r.text:
            write_log(get_data(), url, "filtered")
            return filtered_content
        else:
            write_log(get_data(), url, "allowed")
            return r.text

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
