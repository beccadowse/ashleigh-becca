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
	callAPI = requests.post("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=51.528837,-0.165653&radius=500&type=restaurant&keyword=vegetarian&key=AIzaSyBmr7SG3-JPw7sGZc_J300-NDgECV-4wC0",
	data={"type": [form_data["diet"]]})
	print form_data["diet"] + " restaurants:" #prints if user vegetarian or not
	#print callAPI.text
	results = callAPI.json()["results"] #parse the list of objects returned by the API to JSON and just get the 'results' array
	restaurant_names= [] #empty list to push the names into
	restaurant_map_link = []


	for restaurants in results :
		if (restaurants.has_key("photos")):
			restaurant_names.append(restaurants["name"])
			for links in restaurants["photos"]:
				restaurant_map_link.append(links["html_attributions"][0])
				location = restaurant_map_link


		#restaurant_names.append(restaurants["name"]) #push the names into the list
		#print len(restaurant_names)
		#restuarant_list=restaurant_names
	return render_template("foods.html", restaurant_names = restaurant_names, location = location)


app.run(debug=True)
