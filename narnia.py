from flask import Flask, render_template

# website entry point
app = Flask(__name__)
app.register_blueprint(tabs, url_)

if __name__ == "__main__":
    app.run()
