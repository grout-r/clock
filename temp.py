from lib import DHT as DHT

DHTPin = 11  # define the pin of DHT1

class temp:
    def __init__(self):
        self.dht = DHT.DHT(DHTPin)

    def getTmp(self):
        chk = self.dht.readDHT11(DHTPin)

        if (chk is self.dht.DHTLIB_OK):
            print("DHT11,OK!")
        elif (chk is self.dht.DHTLIB_ERROR_CHECKSUM):  # data check has errors
            print("DHTLIB_ERROR_CHECKSUM!!")
        elif (chk is self.dht.DHTLIB_ERROR_TIMEOUT):  # reading DHT times out
            print("DHTLIB_ERROR_TIMEOUT!")
        else:  # other errors
            print("Other error!")
        return '{:02d}'.format(self.dht.temperature)
