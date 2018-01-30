import yeelight


class Lamp:
    def __init__(self):
        self.desk = yeelight.Bulb("192.168.1.47", duration=1000)
        pass

    def switch_on(self):
        try:
            self.desk.turn_on()
        finally:
            pass
    