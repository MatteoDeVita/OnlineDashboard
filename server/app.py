from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json
import sys

#instantiate the app
app = Flask(__name__)
app.secret_key = "hello"
#app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/users.db'

db = SQLAlchemy(app)
#enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

class Users(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   user = db.Column(db.String(100))
   passw = db.Column(db.String(100))

def __init__(self, user, passw):
   self.user = user
   self.passw = passw

@app.route('/')
def root():
    return redirect(url_for('login'))

@app.route('/login/<username>/<password>')
def login(username, password):
    #value = {'username': username, 'password': password}
    new_user = Users(user=username, passw=password)
    db.session.add(new_user)
    db.session.commit()
    #Users.query.order_by(Users.username).all()
    print(Users.query.order_by(Users.user).all(), flush=True)
    print(new_user.user, flush=True)
    #jsonvalue = jsonify(value)
    #console.log()
    return "coucou"
    #return login

# sanity check route
#@app.route('/ping', methods=['GET'])
#def ping_pong():
#    return 'ppong!! salut a tous'

@app.route('/youtubeSearch/<querry>')
def youtubeSearch(querry):
    url = 'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=' + querry + '&key=AIzaSyDk9VAahqVFWxpTqzYkV104rNMZV8TsQ10'
    response = requests.get(url)
    jsonResponse = response.json()
    dicArray = []
    for item in jsonResponse["items"]:
        dic = {"id": "", "title": ""}
        id = item["id"]
        if "videoId" in id:
            dic["id"] = id["videoId"]
            snippet = item["snippet"]
            if "title" in snippet:
                dic["title"] = snippet["title"]
                dicArray.insert(len(dicArray), dic)
    return jsonify(dicArray)

@app.route('/weather/<city>')
def weather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=fr&appid=14b0797baca6b874f51e3d0d18fbb160'
    response = requests.get(url)
    jsonResponse = response.json()
    dic = {
        "description": "",
        "icon": "",
        "temp": 0,
        "feels_like": 0,
        "wind_speed": ""
    }
    if "weather" in jsonResponse:
        if "description" in jsonResponse["weather"][0]:
            dic["description"] = jsonResponse["weather"][0]["description"]
        if "icon" in jsonResponse["weather"][0]:
            dic["icon"] = "http://openweathermap.org/img/w/" + jsonResponse["weather"][0]["icon"] + ".png"
    if "main" in jsonResponse:
        if "temp" in jsonResponse["main"]:
            dic["temp"] = jsonResponse["main"]["temp"]
        if "feels_like" in jsonResponse["main"]:
            dic["feels_like"] = jsonResponse["main"]["feels_like"]
    if "wind" in jsonResponse:
        if "speed" in jsonResponse["wind"]:
            dic["wind_speed"] = jsonResponse["wind"]["speed"]
    return jsonify(dic)

@app.route('/weatherForecast/<city>')
def weatherForecast(city):
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&units=metric&lang=fr&appid=14b0797baca6b874f51e3d0d18fbb160'
    response = requests.get(url)
    jsonResponse = response.json()["list"][0]
    dic = {
        "description": "",
        "icon": "",
        "temp": 0,
        "feels_like": 0,
        "wind_speed": ""
    }
    if "weather" in jsonResponse:
        if "description" in jsonResponse["weather"][0]:
            dic["description"] = jsonResponse["weather"][0]["description"]
        if "icon" in jsonResponse["weather"][0]:
            dic["icon"] = "http://openweathermap.org/img/w/" + jsonResponse["weather"][0]["icon"] + ".png"
    if "main" in jsonResponse:
        if "temp" in jsonResponse["main"]:
            dic["temp"] = jsonResponse["main"]["temp"]
        if "feels_like" in jsonResponse["main"]:
            dic["feels_like"] = jsonResponse["main"]["feels_like"]
    if "wind" in jsonResponse:
        if "speed" in jsonResponse["wind"]:
            dic["wind_speed"] = jsonResponse["wind"]["speed"]
    return jsonify(dic)

if __name__ == '__main__':
  db.create_all()
  app.run(host="0.0.0.0", debug=True)
