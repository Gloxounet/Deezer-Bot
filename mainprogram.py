import deezer
import txtconverter

client = deezer.Client()
user_list = txtconverter.get_available_user_from_txt()

deezer.resources.Track

def get_user(username) :
    return client.get_user(username)

def get_playlists(user) :
    return user.get_playlists()

def get_tracks(playlist):
    return playlist.get_tracks(limit='1000')

def get_favorite(user) :
    return user.get_tracks(limit='1000')

def get_artist(track):
    return track.get_artist()

#PROGRAM

if __name__ == "__main__" :
    user = client.get_user(matteo)
    user.get_playlists()
