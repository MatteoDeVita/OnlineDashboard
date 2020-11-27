from flask import Flask, jsonify, redirect, url_for
# from flask_mysqldb import MySQL
from flask_cors import CORS
import requests
#configuration
DEBUG = True

#instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
# mysql = MySQL(app)


app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'hourquet'
app.config['MYSQL_DB'] = 'dash_db'

# mysql = MySQL(app)


#enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def root():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return 'login'

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return 'ppong!! salut a tous'

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

if __name__ == '__main__':
        app.run(host="0.0.0.0", debug=True)
