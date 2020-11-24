from flask import Flask, jsonify, redirect, url_for
from flask_mysqldb import MySQL
from flask_cors import CORS

#configuration
DEBUG = True

#instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
mysql = MySQL(app)





app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'hourquet'
app.config['MYSQL_DB'] = 'dash_db'

mysql = MySQL(app)


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
        app.run(host="0.0.0.0", debug=True)
