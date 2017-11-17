from gmusicapi import Mobileclient


class music:
    def __init__(self):
        api = Mobileclient()
        api.login('roman.grout@gmail.com', 'romgroGMAIL95', Mobileclient.FROM_MAC_ADDRESS)

        library = api.get_all_songs()


        url = api.get_stream_url(song_id='bc0c11b1-03ea-30a5-bda8-66906c532373', device_id=None, quality=u'hi')
        print(url)


