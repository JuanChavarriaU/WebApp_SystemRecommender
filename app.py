import streamlit as st
import os 
from spotipy_client import *
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
SCOPE = 'playlist-modify-private,playlist-modify-public,user-top-read'



sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                        redirect_uri=REDIRECT_URI, scope=SCOPE)


st.title("Spotify Playlist Generator")

token_info = sp_oauth.get_cached_token()


if not token_info:
    # Ask user to authenticate
    auth_url = sp_oauth.get_authorize_url()
    st.markdown(f"[Log in with Spotify]({auth_url})")
    
    # Get the authorization code from the URL
    auth_code = st.experimental_get_query_params().get('code', None)
    if auth_code:
        # Exchange auth code for access token
        token_info = sp_oauth.get_access_token(auth_code[0])
        sp = spotipy.Spotify(auth=token_info['access_token'])
else:
    # Token already cached, use it
    sp = spotipy.Spotify(auth=token_info['access_token'])

    # Step 3: Get Spotify Username
    USERNAME = sp.current_user()['id']
    st.write(f"Logged in as: {username}")


#button to submit
if st.button('Generate Playlist'):
    
            spotipy_client = SpotipyClient(CLIENT_ID, CLIENT_SECRET, USERNAME, REDIRECT_URI, SCOPE)

            try:
                spotipy_client.create_recommended_playlist()
                st.success('Playlist created successfully on Spotify!')
            except Exception as e:
                st.error(f"An error occurred: {e}")

