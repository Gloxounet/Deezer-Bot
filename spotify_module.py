import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

simeo="simeo11"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='96b40f6e2f66470a81bb9f2eeb93e233',
                                                           client_secret='24d7f1fe71f441c0952e8b9a6badae69'))


playlists = sp.user_playlists("simeo11")
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None