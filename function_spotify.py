import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='96b40f6e2f66470a81bb9f2eeb93e233',
                                                           client_secret='24d7f1fe71f441c0952e8b9a6badae69'))

def get_playlists(username) :
    playlists = sp.user_playlists(username,limit=50)
    return playlists

def get_tracks(playlist) :
    tracks = sp.playlist_items(playlist,limit=100)
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

if __name__ == "__main__" :
    simeo="simeo11"
    liste = list_playlists(get_playlists(simeo))
    print(get_tracks(liste[0][0]))