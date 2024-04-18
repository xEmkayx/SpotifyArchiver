import spotipy
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
    print("Sucessfully ran the save-discover-weekly script.")
