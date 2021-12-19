from flask import Blueprint, render_template

tabs = Blueprint(__name__, "tabs")


@tabs.route("/")
def owl():
    return render_template("index.html")


@tabs.route("/covid")
def covid():
    f = open("database.txt", "r")
    return render_template("covid.html", content=f.readline())
