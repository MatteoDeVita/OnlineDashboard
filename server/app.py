from flask import Flask, jsonify, redirect, url_for
from flask_cors import CORS

#configuration
DEBUG = True

#instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

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

if __name__ == '__main__':
        app.run()
