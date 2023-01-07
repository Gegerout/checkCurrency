from flask import Flask, render_template
import currencyRequest

app = Flask(__name__)

@app.route("/")
def index():
    result = currencyRequest.sendRequest()
    return render_template("index.html", result=result)

app.run(host='0.0.0.0', port=8080)