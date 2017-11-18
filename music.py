from gmusicapi import Mobileclient
import vlc
import json
import random


class Music:
    def __init__(self):
        self.index = 0
        self.tracks = []
        self.api = Mobileclient()
        self.api.login('roman.grout@gmail.com', 'romgroGMAIL95', Mobileclient.FROM_MAC_ADDRESS)

    def load_random(self):
        stations = self.api.get_all_stations()
        station = random.choice(stations)
        self.tracks = self.api.get_station_tracks(station["id"])

    def play_random(self):
        url = self.api.get_stream_url(self.tracks[self.index]['nid'], device_id=None, quality=u'hi')
        self.player = vlc.MediaPlayer(url)
        self.player.play()

    def update(self):
        # todo update
        pass

    def next_song(self):
        self.index += 1
        self.play_random()
        pass
