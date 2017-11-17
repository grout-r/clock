from datetime import datetime

from lib.Adafruit_LCD1602 import Adafruit_CharLCD
from lib.PCF8574 import PCF8574_GPIO


class lcd:
    def __init__(self):
        PCF8574_address = 0x27
        PCF8574A_address = 0x3F

        try:
            self.mcp = PCF8574_GPIO(PCF8574_address)
        except:
            try:
                self.mcp = PCF8574_GPIO(PCF8574A_address)
            except:
                print('I2C Address Error !')
                exit(1)
        # Create LCD, passing in MCP GPIO adapter.
        self.lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4, 5, 6, 7], GPIO=self.mcp)
        self.mcp.output(3, 1)
        self.lcd.begin(16, 2)
        self.lcd.setCursor(0, 0)

    def printWelcome(self):
        self.lcd.message('Init done.')

    def update(self, tmp):
        self.lcd.setCursor(0, 0)

        self.lcd.message(datetime.now().strftime('%H:%M:%S\nIN:' + tmp.getTmp() + "C"))
