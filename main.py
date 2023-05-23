from flask import Flask, render_template, request
from Pintrest import Pintrest
from base64 import b64decode

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route("/download",methods=["POST","GET"])
def download():
    if request.method == "GET":
        return render_template("Download.html",data={'type':request.args["type"],"url":b64decode(request.args["data"]).decode('ascii')})
    elif request.method == "POST":
        url = b64decode(request.form["url"]).decode('ascii')
        p = Pintrest(url)
        return p.get_media_Link()

if __name__ == "__main__":
    app.run(debug=True)