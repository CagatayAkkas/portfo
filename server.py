from asyncore import write
import email
import csv
from email import message
from turtle import pos
from unicodedata import name
from black import NewLine
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open("database.txt", mode="a") as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]

        file = database.write(f"\n{email},{name},{message}")


def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as database2:
        name = data["name"]
        email = data["email"]
        message = data["message"]

        csv_writer = csv.writer(
            database2,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_writer.writerow([email, name, message])


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "did not save to database"

    else:
        return "something wrong"
