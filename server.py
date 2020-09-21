from flask import Flask, redirect, render_template, request
import csv
from os import path

app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
	return render_template("index.html")

@app.route("/save",methods=["POST"])
def save():
	fields = ["name","email"]
	fileexist = path.isfile("data.csv")
	with open("data.csv","a") as datafile:
		writer = csv.DictWriter(datafile, fieldnames=fields)

		if not fileexist:
			writer.writeheader()
		writer.writerow({"name":request.form["name"],"email":request.form["email"]})
	return redirect("/")
