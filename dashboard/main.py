from flask import Blueprint, render_template 
from flask_login import login_required, current_user
app = Flask(__name__)
@app.route("/")
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

if name == "main":
    # Only for debugging while developing
   app.run(host='0.0.0.0', debug=True, port=5000)


#from flask import Flask
#app = Flask(__name__)
#
#@app.route("/")
#def hello():
#    return "Hello World from Flask"
#
#if __name__ == "__main__":
#    # Only for debugging while developing
#    app.run(host='0.0.0.0', debug=True, port=5000)