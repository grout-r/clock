from flask import Flask
import schedule
import time
from threading import Thread
import RPi.GPIO
from pcf8574 import PCF8574
import Adafruit_CharLCD as LCD

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/add")
def add():
    schedule.every(1).seconds.do(ring)
    return "coucou"


def ring():
    print("Drrrrrriiinng")


def run_scheduled():
    while 1:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':

    # PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
    # PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
    # # Create PCF8574 GPIO adapter.
    # try:
    #     mcp = PCF8574(PCF8574_address)
    # except:
    #     print("Wrong")
    #     try:
    #          mcp = PCF8574(PCF8574A_address)
    #     except:
    #         print('I2C Address Error ! #1')
    #         exit(1)
    #
    # # Create LCD, passing in MCP GPIO adapter.
    # lcd = LCD(pin_rs=0, pin_e=2, pins_db=[4, 5, 6, 7], GPIO=mcp)

    # Raspberry Pi pin configuration:
    lcd_rs = 21  # Note this might need to be changed to 21 for older revision Pi's.
    lcd_en = 22
    lcd_d4 = 25
    lcd_d5 = 24
    lcd_d6 = 23
    lcd_d7 = 18
    lcd_backlight = 4

    # BeagleBone Black configuration:
    # lcd_rs        = 'P8_8'
    # lcd_en        = 'P8_10'
    # lcd_d4        = 'P8_18'
    # lcd_d5        = 'P8_16'
    # lcd_d6        = 'P8_14'
    # lcd_d7        = 'P8_12'
    # lcd_backlight = 'P8_7'

    # Define LCD column and row size for 16x2 LCD.
    lcd_columns = 16
    lcd_rows = 2

    # Alternatively specify a 20x4 LCD.
    # lcd_columns = 20
    # lcd_rows    = 4

    # Initialize the LCD using the pins above.
    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                               lcd_columns, lcd_rows, lcd_backlight)

    # Print a two line message
    lcd.message('Hello\nworld!')

    t = Thread(target=run_scheduled)
    t.start()
    app.run(host='0.0.0.0')

