from flask import Flask

# website entry point
app = Flask(__name__)


@app.route("/narnia")
def narnia():
    return "<h1>Welcome to Narnia!<h1>"


if __name__ == "__main__":
    app.run()
