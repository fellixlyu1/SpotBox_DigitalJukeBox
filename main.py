import spotipy
from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, render_template, request

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
username = os.getenv("USERNAME")
redirect_uri = os.getenv("REDIRECT_URI")

app = Flask(__name__)


def get_track_uri(track_name, artist_name):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=redirect_uri))

    query = "track:{}, artist:{}".format(track_name, artist_name)
    results = sp.search(q=query, type="track", limit=1)
    if results['tracks']['items']:
        return results['tracks']['items'][0]['uri']
    else:
        return None


@app.route("/", methods=['GET'])
def index():
    return render_template('spot_box.html')


@app.route("/add_to_queue", methods=['POST'])
def add_to_queue():
    track_name = request.form.get('track')
    artist_name = request.form.get('artist')
    scope = 'user-modify-playback-state'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=redirect_uri,
                                                   scope=scope))
    track_uri = get_track_uri(track_name, artist_name)

    if track_uri:
        sp.add_to_queue(track_uri)
        track_display = sp.track(track_uri)
        track_name = track_display['name']
        track_artist = track_display['artists'][0]['name']
        track_image = track_display['album']['images'][0]['url']
        return render_template("add_to_queue.html", track=track_name, artist=track_artist, cover_image=track_image)
    else:
        return str("Track could not be found")


def image():
    scope = "user-read-currently-playing"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=redirect_uri,
                                                   scope=scope, username=username))
    current_song = sp.current_user_playing_track()
    album_image = current_song["item"]["album"]["images"][0]["url"]
    return album_image


@app.route("/playback", methods=["GET"])
def current_playback():
    scope = "user-read-currently-playing"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=redirect_uri,
                                                   scope=scope, username=username))
    current_song = sp.current_user_playing_track()
    song = current_song["item"]
    artist = current_song["item"]["artists"][0]["name"]
    image_url = image()
    return render_template("image.html", song=song["name"], artist=artist, album_image=image_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
