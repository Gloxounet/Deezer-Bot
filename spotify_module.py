import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

simeo="simeo11?si=N0VDOPPhTVGm9JbDz1eRKQ"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='96b40f6e2f66470a81bb9f2eeb93e233',
                                                           client_secret='24d7f1fe71f441c0952e8b9a6badae69'))

print(sp)
print(sp.user(simeo))