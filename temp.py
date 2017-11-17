from lib import DHT as DHT

DHTPin = 11  # define the pin of DHT1


class temp:
    def __init__(self):
        self.dht = DHT.DHT(DHTPin)

    def getTmp(self):
        self.dht.readDHT11(DHTPin)
        return '{:02d}'.format(self.dht.temperature)
