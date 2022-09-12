# SpotifyArchiver

This simple and lightweight script allows you to simply archive playlists on Spotify by appending the contents of one playlist 
to another one.
It was made with Spotify's Release Radar and Discover Weekly playlists in mind, but it's applicable to every playlist.
For this, simply copy one of the save files and edit the playlist IDs as explained below.

# Installation
This script was made for execution on a server or similar in mind, where it can be executed periodically. Personally, I run it 
on a raspberry pi. Since it's a very light script, there's little to no change in performance. 
Of course, it's also possible to run this script only when needed.
An instance of python3 is required.
---
To download the script run
```
git clone <link>
```
Next, you need to install the requirements; to do so, simply run
```
pip install -r requirements.txt
```
inside the project folder.

# Getting Spotify IDs
Now you need to get your Spotify authorization IDs. As this section is prone to change, please refer to the official
documentation of either Spotify or spotipy (the python package used for this script):
- [Spotify for Developers](https://developer.spotify.com/documentation/general/guides/authorization/)
- [Spotipy](https://spotipy.readthedocs.io/en/master/#authorization-code-flow)

Aditionally, you also need an "archive playlist" to which the tracks should get appended to.

# Configuration
Now that you have all the required IDs, you need to place them at their specific places.
In the ```./data/``` folder, rename the ```example_auth.py``` and ```example_data_constants.py``` to ```auth.py``` and ```data_constants.py```respectively. 
The ```auth.py``` file contains your authorization IDs (client id and client secret). You can safely ignore the redirection uri.
The ```data_constants.py``` file contains the IDs for your playlists. Simply edit them where needed.

# Running the script
Once this is done, you can simply execute the script by typing 
```
python save_discover_weekly.py
 ```
or 
```
python save_release_radar.py
 ```
into the command line (note that you might need to replace ```python``` by ```python<version_no>``` (e.g. ```python3.10```). This might occur when you have multiple instances of python installed)

# Running the script periodically with a cronjob
One example to run this script periodically (as intended) is by running it as a cronjob (Linux).

Here are two simple examples for a cronjob to run this script:
- ``` 0 12   *   *   1 cd <script location> && python save_discover_weekly.py ```
- ``` 0 12   *   *   5 cd <script location> && python save_release_radar.py ```

These scripts are run on 12.00PM at monday (represented by the 1 in the first script) and friday (5 in the second script). These are the days their respective playlists get updated by Spotify.