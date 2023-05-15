from spotipy.oauth2 import SpotifyOAuth
import spotipy
from bs4 import BeautifulSoup

from urllib.request import urlopen

BILLBOARD_ADRESS = "https://www.billboard.com/charts/hot-100/"
SP_CLIENT_ID = "778ca90c2482451691ded264c82cc889"
SP_CLIENT_SECRET = "21f941345d294ff2bd06cf9e2fc302eb"

time_date = input(
    "What year you would like to travel to? Use YYYY-MM-DD format: ")

url = BILLBOARD_ADRESS + time_date
print(url)
page = urlopen(url)
html_bytes = page.read()
contents = html_bytes.decode("utf-8")


soup = BeautifulSoup(contents, "html.parser")

songs_names_spans = soup.select("li ul li h3")

songs = []

songs = [song.getText().strip() for song in songs_names_spans]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SP_CLIENT_ID,
        client_secret=SP_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
song_uris = []
year = time_date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(
    user=user_id, name=f"{time_date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
