import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

simeo="simeo11"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='96b40f6e2f66470a81bb9f2eeb93e233',
                                                           client_secret='24d7f1fe71f441c0952e8b9a6badae69'))


def get_playlists(username) :
    playlists = sp.user_playlists(username)
    return playlists

def get_tracks(playlist) :
    tracks = sp.playlist_items(playlist)
    track_list = []
    for i in tracks['items'] :
        single_name = i['track']['name']
        author_name = i['track']['artists'][0]['name']
        track_list.append(single_name + " " + author_name)
    return track_list

def list_playlists(playlist) :
    """
    return a [(id,name)] list
    """
    liste = []
    for i in playlist['items'] :
        idd = i["id"]
        name = i["name"]
        liste.append((idd,name))
    return liste




# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None

