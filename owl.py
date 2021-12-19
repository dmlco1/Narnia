from flask import Flask, render_template
from tabs import tabs
import covid_stats

# website entry point

app = Flask(__name__)
app.register_blueprint(tabs, url_prefix="/owl")

if __name__ == "__main__":
    for i in range(0):
        covid_stats
    app.run(debug=True)
