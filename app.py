import os
from flask import Flask, render_template
import currencyRequest

app = Flask(__name__)

@app.route("/")
def index():
    result = currencyRequest.sendRequest()
    return render_template("index.html", result=result)

if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4444)))