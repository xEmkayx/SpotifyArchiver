from flask import Flask, request

import archive_playlist
import util.token_util
from constants.constants import ScriptType

app = Flask(__name__)


@app.route('/getRedirectUrl')
def get_auth_url():
    return util.token_util.get_auth_url()


@app.route('/callback', methods=['POST'])
def callback():
    if request.is_json:
        url = request.get_json()
        print(url['url'])
        util.token_util.generate_token_from_url(url['url'])
        return "Abruf erfolgreich", 200

    return "Anforderung enthält kein JSON!", 400


@app.route('/run/release-radar')
def run_release_radar():
    return archive_playlist.main(ScriptType.RELEASE_RADAR)


@app.route('/run/discover-weekly')
def run_discover_weekly():
    return archive_playlist.main(ScriptType.DISCOVER_WEEKLY)

# todo:
# - endpoint to check if token file exists
# - endpoint to check how long till token expires


if __name__ == '__main__':
    app.run(host='localhost', port=8123)
