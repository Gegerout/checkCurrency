from flask import Flask, render_template
import currencyRequest

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    result = currencyRequest.sendRequest()
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()
