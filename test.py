
from flask import Flask, flash, redirect, render_template, request, url_for
import os
from flask import send_from_directory

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/favicon.jpg')
@app.route('/')
@app.route("/home")
def home():
    return "hello world"

if __name__ == '__main__':
    app.secret_key = "ItIsASecret"
    app.debug = True
    app.run