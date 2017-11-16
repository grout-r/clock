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

    PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
    PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
    # Create PCF8574 GPIO adapter.
    try:
        mcp = PCF8574(0, PCF8574_address)
    except:
        print("Wrong")
        try:
             mcp = PCF8574(0, PCF8574A_address)
        except:
            print('I2C Address Error ! #1')
            exit(1)

    # Create LCD, passing in MCP GPIO adapter.
    lcd = LCD(pin_rs=0, pin_e=2, pins_db=[4, 5, 6, 7], GPIO=mcp)

    t = Thread(target=run_scheduled)
    t.start()
    app.run(host='0.0.0.0')

