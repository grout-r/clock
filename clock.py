from flask import Flask
import schedule
import time
from threading import Thread

from lcd import lcd
from temp import temp
from music import Music
import RPi.GPIO as GPIO

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
        lcd.update(tmp)
        if GPIO.input(buttonPin) == GPIO.LOW:
            music.next_song()
        time.sleep(1)

if __name__ == '__main__':
    lcd = lcd()
    tmp = temp()

    music = Music()
    music.load_random()
    music.play_random()

    buttonPin = 12  # define the buttonPin
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:
            print('led on ...')
        else:
            print('led off ...')
        time.s

    t = Thread(target=loop)
    t.start()
    app.run(host='0.0.0.0')

