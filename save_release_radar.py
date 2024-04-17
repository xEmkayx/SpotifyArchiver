import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

scope = 'playlist-modify-public playlist-modify-private'
load_dotenv()


def main():
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
        redirect_uri=os.getenv('REDIRECT_URI'),
        scope=scope,
        open_browser=False))

    release_radar_id = os.getenv('RELEASE_RADAR_ID')
    release_radar_archive_id = os.getenv('RELEASE_RADAR_ARCHIVE_ID')

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
    print("Sucessfully ran the save-release-radar script.")
