import spotipy
import os
from dotenv import load_dotenv

from constants.constants import *
from util.token_util import load_token, refresh_if_needed

scope = 'playlist-modify-public playlist-modify-private'
load_dotenv()


def main(script_type: ScriptType):
    token_info = load_token(CACHE_FILE_NAME)

    if not token_info:
        print('No token')
        return "There is no (valid) token", 401

    token_info = refresh_if_needed(token_info)

    spotify = spotipy.Spotify(auth=token_info['access_token'])

    if script_type == ScriptType.DISCOVER_WEEKLY:
        playlist_id = os.getenv('DISCOVER_WEEKLY_ID')
        archive_playlist_id = os.getenv('DISCOVER_WEEKLY_ARCHIVE_ID')
    else:
        playlist_id = os.getenv('RELEASE_RADAR_ID')
        archive_playlist_id = os.getenv('RELEASE_RADAR_ARCHIVE_ID')

    dw = spotify.playlist(playlist_id)
    position = 0
    dw_tracks = []
    for track in dw['tracks']['items']:
        track_id = track['track']['id']
        dw_tracks.append(track_id)

    spotify.playlist_add_items(playlist_id=archive_playlist_id,
                               items=dw_tracks, position=position)

    return "Success", 200


if __name__ == '__main__':
    main(ScriptType.RELEASE_RADAR)
    print("Sucessfully ran the script.")
