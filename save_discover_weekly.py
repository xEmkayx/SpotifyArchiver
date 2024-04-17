import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

scope = 'playlist-modify-public playlist-modify-private'


def main():
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
        redirect_uri=os.getenv('REDIRECT_URI'),
        scope=scope,
        open_browser=False))

    discover_weekly_id = os.getenv('DISCOVER_WEEKLY_ID')
    discover_weekly_archive_id = os.getenv('DISCOVER_WEEKLY_ARCHIVE_ID')

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
