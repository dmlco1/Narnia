from flask import Blueprint, render_template

tabs = Blueprint(__name__, "tabs")


@tabs.route("/")
def narnia():
    return render_template("index.html")


@tabs.route("/covid")
def covid():
    return render_template("graph.html")
