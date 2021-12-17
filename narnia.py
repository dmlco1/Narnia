from flask import Flask, render_template

# website entry point
app = Flask(__name__)


@app.route("/narnia")
def narnia():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
