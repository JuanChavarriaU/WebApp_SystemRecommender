import streamlit as st
import os 
from spotipy_client import *


REDIRECT_URI = "http://127.0.0.1:5000/"
SCOPE = 'playlist-modify-private,playlist-modify-public,user-top-read'

st.title("Spotify Playlist Generator")

CLI_ID = st.text_input("Enter your Spotify Client ID:")
CLI_SEC = st.text_input("Enter your spotify Client Secret:", type='password')
USERNAME = st.text_input("Enter your Username:")

#button to submit
if st.button('Generate Playlist'):
    if CLI_ID and CLI_SEC and USERNAME:
        try: 
            #initialize the constructor
            sp = SpotipyClient(CLI_ID, CLI_SEC, USERNAME, REDIRECT_URI ,SCOPE)

            sp.create_recommended_playlist()

            st.success('Playlist created successfully on Spotify!')
        except Exception as e:
            st.error(f"An error occurred {e}")
    else:
        st.warning('Please provide Client ID, Client Secret and Username')

