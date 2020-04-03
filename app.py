from flask import Flask
from flask import render_template
import pyrebase

config = {
    "apiKey": "AIzaSyCZUj4DQvwomiIsgQRxb6Wh_TaP4Njz6eE",
    "authDomain": "portfolio-website-54a58.firebaseapp.com",
    "databaseURL": "https://portfolio-website-54a58.firebaseio.com",
    "projectId": "portfolio-website-54a58",
    "storageBucket": "portfolio-website-54a58.appspot.com",
    "messagingSenderId": "227450648359",
    "appId": "1:227450648359:web:79161610ebf986b77d5b02"
}

firebase = pyrebase.initialize_app(config)

username = 'Shahrin'

# Get data related to the selected user
def get_data(username):
    db = firebase.database()
    show = db.child('users').get()
    user = show.val()[username]
    return user

# Pass data related to the selected project
def project_data(projectname):
    db = firebase.database()
    show = db.child('users').child(username).child('project').get()
    for x in show.each():
        if x.val()['projectname'] == projectname:
            return x.val()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=get_data(username))

@app.route('/landing/<project>')
def landing(project):
    return render_template('landing.html', project=project_data(project))

if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.143')