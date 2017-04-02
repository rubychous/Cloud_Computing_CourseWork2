from app import app
from flask_navigation import Navigation
from flask import render_template, request
import unirest
from forms import MessageForm
from app import database
import os

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")

@app.route('/emotion/')
def emotion():
	return render_template("my_form.html",mood='Neutral',form=MessageForm())

@app.route('/emotion/', methods=['POST'])
def emotion_post():
	msg = request.form['message']
	response = unirest.post("https://community-sentiment.p.mashape.com/text/",
	  headers={
	    "X-Mashape-Key": os.environ['APITOKEN'],
	    "Content-Type": "application/x-www-form-urlencoded",
    	"Accept": "application/json"
    	},
  		params={
    	"txt": msg
  		}
	)
	return render_template("my_form.html",mood=response.body['result']['sentiment'],form=MessageForm())


nav = Navigation(app)
nav.Bar('top', [
nav.Item('Home','index'),
nav.Item('Emotion App','emotion'),
nav.Item('Visualization','polynomial'),
nav.Item('Database','get_db_info')
#nav.Item('Database','get_all_collections'),
#nav.Item('Document','get_sample_document'),
#nav.Item('London_Methods','get_collection_methods_and_attributes'),
#nav.Item('DB_Methods','get_db_methods_and_attributes')
])

