import os 
from flask import Flask, flash, request, render_template
from spotipy_client import *
from dotenv import load_dotenv

REDIRECT_URI = "http://127.0.0.1:5000/"
SCOPE = 'playlist-modify-private,playlist-modify-public,user-top-read'

app = Flask(__name__)
app.secret_key = os.getnev("SECRET_KEY")

@app.route('/', methods=["GET", "POST"])
def client_auth_form():
    if request.method == "POST":
        CLI_ID = request.form['cl_id']
        CLI_SEC = request.form['cl_secret']
        USERNAME = request.form['username']

        sp = SpotipyClient(CLI_ID, CLI_SEC, USERNAME, REDIRECT_URI, SCOPE)
        
        sp.create_recommended_playlist()
        flash('Playlist created on Spotify!')

        return render_template('home.html')
   





