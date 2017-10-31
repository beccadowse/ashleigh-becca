
from flask import Flask, render_template, request
import requests
import json

app = Flask ("MyApp")

@app.route("/") #the URL is just a slash
def hello (): #a function that returns hello world
	return render_template("hello.html")

@app.route("/foods", methods=["POST"])
def show_veg_restaurants():

	form_data = request.form
	callAPI = requests.post("https://maps.googleapis.com/maps/api/place/textsearch/json?query=Vegetarian&sensor=true&location=51.50020.1332&radius=20&type=restaurant&keyword=vegetarian&key=AIzaSyCnQcaSqXzBMfcO_4eWK8Oh1B3gFUgKof8",
	data={"type": [form_data["diet"]]})
	print form_data["diet"] #print if user is vegetarian
	print callAPI.text #print in terminal as unicode
	api_results = callAPI.json()["results"] #parse the api results to a JSON and set variable to return just the object "results"
	for restaurant in api_results :
		print restaurant["name"]
		
	return render_template("foods.html")

app.run(debug=True)
