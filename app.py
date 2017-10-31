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
	callAPI = requests.post("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=vegetarian&key=AIzaSyBmr7SG3-JPw7sGZc_J300-NDgECV-4wC0",
	data={"type": [form_data["diet"]]})
	print form_data["diet"] #prints if user vegetarian or not
	#print callAPI.text
	results = callAPI.json()["results"] #parse the array of objects returned by the API to JSON and just get the 'results' array
	#print restaurants
	for restaurants in results :
		print restaurants["name"]

	return render_template("foods.html")


app.run(debug=True)
