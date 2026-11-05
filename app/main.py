from flask import Flask, render_template

app = Flask(__name__, static_folder="../public", static_url_path="")


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
