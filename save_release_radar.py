import spotipy
from spotipy.oauth2 import SpotifyOAuth
from data.auth import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from data.data_constants import release_radar_id, release_radar_archive_id
import json

scope = 'playlist-modify-public playlist-modify-private'


def main():
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                        redirect_uri=REDIRECT_URI, scope=scope))

    rr = spotify.playlist(release_radar_id)
    position = 0
    rr_tracks = []
    for track in rr['tracks']['items']:
        track_id = track['track']['id']
        rr_tracks.append(track_id)

    spotify.playlist_add_items(playlist_id=release_radar_archive_id,
                               items=rr_tracks, position=position)


if __name__ == '__main__':
    main()
