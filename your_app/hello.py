from flask import Flask, render_template, request
import requests

app = Flask ("MyApp")

@app.route("/") #the URL is just a slash
def hello (): #a function that returns hello world
	return render_template("hello.html")

@app.route("/foods", methods=["POST"])
def show_veg_restaurants():
	form_data = request.form
	requests.post(
		"https://maps.googleapis.com/maps/api/place/textsearch/json?query=Vegetariansensor=true&location=51.5002, 0.1332&radius=20&type=restaurant&keyword=vegetarian&key=YAIzaSyDdKwRrCOG__Dwa3d8iAt_wpLQjIHewJ48",
		data={"type": [form_data["diet"]]})
	print form_data["diet"]
	return "All OK"

app.run(debug=True)
