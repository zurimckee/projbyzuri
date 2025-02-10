import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="c7e1d7b3540f4d9287407c5a47b450b7",
                                                           client_secret="a6a75e851e5a4cd59ae05d69c1c6f029"))

#results = sp.search(q='dangelo', limit=7)
#for idx, track in enumerate(results['tracks']['items']):
    #print(idx, track['name'])

