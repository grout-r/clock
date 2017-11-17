
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD

class lcd:


    def __init__(self):
        PCF8574_address = 0x27
        PCF8574A_address = 0x3F

        try:
            self.mcp = PCF8574_GPIO(PCF8574_address)
        except:
            print("milieu")
            try:
                self.mcp = PCF8574_GPIO(PCF8574A_address)
                print("apres")
            except:
                print('I2C Address Error !')
                exit(1)
        # Create LCD, passing in MCP GPIO adapter.
        self.lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4, 5, 6, 7], GPIO=mcp)
        self.mcp.output(3, 1)
        self.lcd.begin(16, 2)
        self.lcd.setCursor(0, 0)
        self.lcd.message('Init done.')


    def printWelcome(self):
        lcd.message('Init done.')
