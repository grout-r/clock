from lib import DHT as DHT

DHTPin = 11  # define the pin of DHT1

class temp:
    def __init__(self):
        self.dht = DHT.DHT(DHTPin)
        self.cache = "--C"

    def getTmp(self):
        chk = self.dht.readDHT11(DHTPin)

        if (chk is self.dht.DHTLIB_OK or chk is self.dht.DHTLIB_ERROR_CHECKSUM):
            self.cache = '{:02d}'.format(self.dht.temperature)
        elif (chk is self.dht.DHTLIB_ERROR_TIMEOUT):  # reading DHT times out
            print("DHTLIB_ERROR_TIMEOUT!")
        else:  # other errors
            print("Other error!")
        return "21"
        #return self.cache