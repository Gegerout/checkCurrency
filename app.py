import os
from flask import Flask, redirect, render_template, request, url_for

import currencyRequest

app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "GET":
        result = currencyRequest.sendRequest()

        return render_template("index.html", result=result)

app.run(host='0.0.0.0', port=5000)