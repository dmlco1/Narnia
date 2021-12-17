from flask import Blueprint

tabs = Blueprint("tabs")


@tabs.route("/")
def narnia():
    return "index.html"
