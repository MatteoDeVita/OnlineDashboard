from flask_cors import CORS
import requests
import flask
import os
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import json
import sys
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

#configuration
DEBUG = True
CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

#instantiate the app
app = flask.Flask(__name__)
# app.config.from_object(__name__)
app.secret_key = "hello"

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
    return flask.redirect(flask.url_for('login'))

@app.route('/test')
def test_api_request():
    if 'credentials' not in flask.session:
        return flask.redirect('authorize')

    # Load credentials from the session.
    credentials = google.oauth2.credentials.Credentials(
        **flask.session['credentials'])

    youtube = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials)

    channel = youtube.channels().list(mine=True, part='snippet').execute()

    # Save credentials back to session in case access token was refreshed.
    # ACTION ITEM: In a production app, you likely want to save these
    #              credentials in a persistent database instead.
    flask.session['credentials'] = credentials_to_dict(credentials)

    return flask.jsonify(**channel)

@app.route('/authorize')
def authorize():
    # Create flow instance to manage the OAuth 2.0 Authorization Grant Flow steps.
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES)

    # The URI created here must exactly match one of the authorized redirect URIs
    # for the OAuth 2.0 client, which you configured in the API Console. If this
    # value doesn't match an authorized URI, you will get a 'redirect_uri_mismatch'
    # error.
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True)

    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true')

    # Store the state so the callback can verify the auth server response.
    flask.session['state'] = state

    return flask.redirect(authorization_url)


@app.route('/oauth2callback')
def oauth2callback():
    # Specify the state when creating the flow in the callback so that it can
    # verified in the authorization server response.
    state = flask.session['state']

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True)

    # Use the authorization server's response to fetch the OAuth 2.0 tokens.
    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)

    # Store credentials in the session.
    # ACTION ITEM: In a production app, you likely want to save these
    #              credentials in a persistent database instead.
    credentials = flow.credentials
    flask.session['credentials'] = credentials_to_dict(credentials)

    return flask.redirect(flask.url_for('test_api_request'))


@app.route('/revoke')
def revoke():
  if 'credentials' not in flask.session:
    return ('You need to <a href="/authorize">authorize</a> before ' +
            'testing the code to revoke credentials.')

  credentials = google.oauth2.credentials.Credentials(
    **flask.session['credentials'])

  revoke = requests.post('https://oauth2.googleapis.com/revoke',
      params={'token': credentials.token},
      headers = {'content-type': 'application/x-www-form-urlencoded'})

  status_code = getattr(revoke, 'status_code')
  if status_code == 200:
    return('Credentials successfully revoked.' + print_index_table())
  else:
    return('An error occurred.' + print_index_table())


@app.route('/clear')
def clear_credentials():
    if 'credentials' in flask.session:
        del flask.session['credentials']
    return ('Credentials have been cleared.<br><br>' +
            print_index_table())


def credentials_to_dict(credentials):
    return {'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes}

def print_index_table():
    return ('<table>' +
            '<tr><td><a href="/test">Test an API request</a></td>' +
            '<td>Submit an API request and see a formatted JSON response. ' +
            '    Go through the authorization flow if there are no stored ' +
            '    credentials for the user.</td></tr>' +
            '<tr><td><a href="/authorize">Test the auth flow directly</a></td>' +
            '<td>Go directly to the authorization flow. If there are stored ' +
            '    credentials, you still might not be prompted to reauthorize ' +
            '    the application.</td></tr>' +
            '<tr><td><a href="/revoke">Revoke current credentials</a></td>' +
            '<td>Revoke the access token associated with the current user ' +
            '    session. After revoking credentials, if you go to the test ' +
            '    page, you should see an <code>invalid_grant</code> error.' +
            '</td></tr>' +
            '<tr><td><a href="/clear">Clear Flask session credentials</a></td>' +
            '<td>Clear the access token currently stored in the user session. ' +
            '    After clearing the token, if you <a href="/test">test the ' +
            '    API request</a> again, you should go back to the auth flow.' +
            '</td></tr></table>')

@app.route('/login/<username>/<password>')
def login(username, password):
    test_user = Users.query.filter_by(user=username).first()
    if(test_user != None):
        print(test_user.user,"-> [USER EXIST]", flush=True)
        if(test_user.passw != password):
            print(password,"-> [INCORRECT PASSWORD]", flush=True)
            return("FAILURE")
        elif(test_user.passw == password):
            print("[CONNECTION OK]", flush=True)
            value = {'username': test_user.user, 'password': test_user.passw}
            return (jsonify(value))
    elif(test_user == None):
        new_user = Users(user=username, passw=password)
        db.session.add(new_user)
        db.session.commit()
        print(new_user.user,"-> [USER CREATED]\n[CONNECTION OK]", flush=True)
        value = {'username': new_user.user, 'password': new_user.passw}
        return (jsonify(value))

# sanity check route
#@app.route('/ping', methods=['GET'])
#def ping_pong():
#    return 'ppong!! salut a tous'

@app.route('/youtubeConnect')
def youtubeConnect():
    state = flask.session['state']
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=['https://www.googleapis.com/auth/youtube.force-ssl'],
        state=state)
    flow.flask.redirect_uri = flask.flask.url_for('oauth2callback', _external=True)

    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)

    # Store the credentials in the session.
    # ACTION ITEM for developers:
    #     Store user's access and refresh tokens in your data store if
    #     incorporating this code into your real app.
    credentials = flow.credentials
    flask.session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes}

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
    print(dicArray[0])
    return flask.jsonify(dicArray[0])

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
    return flask.jsonify(dic)

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
    return flask.jsonify(dic)

@app.route('/youtubeChannel/<username>')
def youtubeChannel(username):
    response = requests.get("https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&forUsername=" + username+ "&key=AIzaSyDk9VAahqVFWxpTqzYkV104rNMZV8TsQ10")
    jsonResponse = response.json()
    dic = {
        "title": "",
        "description": "",
        "thumbnail_url": "",
        "country": "",
        "viewCount": "",
        "subscriberCount": "",
        "videoCount": "",        
    }
    item = jsonResponse["items"][0]
    if "snippet" in item:
        snippet = item["snippet"]
        if "title" in snippet:
            dic["title"] = snippet["title"]
        if "description" in snippet:
            dic["description"] = snippet["description"]
        if "thumbnails" in snippet:
            thumbnails = snippet["thumbnails"]
            if "default" in thumbnails:
                dic["thumbnail_url"] = thumbnails["default"]["url"]
        if "country" in snippet:
            dic["country"] = snippet["country"]
    if "statistics" in item:
        statistics = item["statistics"]
        if "viewCount" in statistics:
            dic["viewCount"] = statistics["viewCount"]
        if "subscriberCount" in statistics:
            dic["subscriberCount"] = statistics["subscriberCount"]
        if "videoCount" in statistics:
            dic["videoCount"] = statistics["videoCount"]
    return flask.jsonify(dic)

if __name__ == '__main__':
    db.create_all()    
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    app.run(host="0.0.0.0", debug=True)
