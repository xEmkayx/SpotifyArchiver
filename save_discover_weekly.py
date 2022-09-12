import spotipy
from spotipy.oauth2 import SpotifyOAuth
from data.auth import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from data.data_constants import discover_weekly_archive_id, discover_weekly_id
import json

scope = 'playlist-modify-public playlist-modify-private'


def main():
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                        redirect_uri=REDIRECT_URI, scope=scope))

    dw = spotify.playlist(discover_weekly_id)
    position = 0
    dw_tracks = []
    for track in dw['tracks']['items']:
        track_id = track['track']['id']
        dw_tracks.append(track_id)

    spotify.playlist_add_items(playlist_id=discover_weekly_archive_id,
                               items=dw_tracks, position=position)


if __name__ == '__main__':
    main()
