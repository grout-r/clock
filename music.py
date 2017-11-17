from gmusicapi import Mobileclient


api = Mobileclient()
api.login('roman.grout@gmail.com', 'romgroGMAIL95', Mobileclient.FROM_MAC_ADDRESS)

library = api.get_all_songs()

for track in library:
    print(track)

