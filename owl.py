from flask import Flask, render_template

from tabs import tabs

# website entry point

app = Flask(__name__)
app.register_blueprint(tabs, url_prefix="/owl")

if __name__ == "__main__":
    app.run(debug=True)
