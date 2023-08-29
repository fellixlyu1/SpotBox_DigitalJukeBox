import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

username = "username"  # Use your spotify account username
CLIENT_ID = "client_id"  # Create a developer portal through Spotify to create client_id
CLIENT_SECRET = "client_secret"  # Create a developer portal through Spotify to create client_secret
redirect_uri = "redirect_uri"  # Use a callback server, typically a localhost


def get_track_uri(track_name):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=redirect_uri))

    query = "track:{} ".format(track_name)
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
    track_name = request.form.get('query')
    scope = 'user-modify-playback-state'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=redirect_uri,
                                                   scope=scope))
    track_uri = get_track_uri(track_name)

    if track_uri:
        sp.add_to_queue(track_uri)
        return jsonify({"message": "Track added to queue"})
    else:
        return jsonify({"message": "Track not found or error in adding to queue"})


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
    return f"Current song: {artist} - {song['name']}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
