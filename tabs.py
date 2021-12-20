from flask import Blueprint, render_template

tabs = Blueprint(__name__, "tabs")


@tabs.route("/")
def owl():
    return render_template("index.html")


@tabs.route("/covid")
def covid():
    file = open("database.txt", "r")
    content = file.readlines()
    return render_template("covid.html", total_cases=content[0],
                           new_cases=content[1],
                           per_million_cases=content[2],
                           total_deaths=content[3],
                           new_deaths=content[4],
                           total_doses=content[5],
                           full_vaccination=content[6],
                           location=content[7])
