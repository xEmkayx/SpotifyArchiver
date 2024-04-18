import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

from constants.constants import CACHE_FILE_NAME
from util.token_util import load_token, refresh_if_needed

scope = 'playlist-modify-public playlist-modify-private'
load_dotenv()


def main():
    token_info = load_token(CACHE_FILE_NAME)

    if not token_info:
        print('There is no token')
        return

    token_info = refresh_if_needed(token_info)

    spotify = spotipy.Spotify(auth=token_info['access_token'])

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
