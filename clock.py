from flask import Flask
import schedule
import time
from threading import Thread
import RPi.GPIO
from lcd import lcd

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


def loop():
    while True:
        schedule.run_pending()
        lcd.update()
        time.sleep(1)

if __name__ == '__main__':
    lcd = lcd()
    lcd.printWelcome()

    t = Thread(target=loop)
    t.start()
    app.run(host='0.0.0.0')

