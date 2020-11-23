- setup
```
sudo npm install -g @vue/cli@3.7.0 &&
sudo apt-get install python3-venv &&
cd server &&
python3 -m venv env &&
source env/bin/activate &&
pip3 install Flask==1.0.2 Flask-Cors==3.0.7
```

- run the app
```
cd server &&
source env/bin/activate &&
(env)$ python app.py
```

- run the ui
```
cd client &&
npm run serve
```
