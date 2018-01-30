from flask import Flask, request
import schedule
import time
from threading import Thread

from lcd import lcd
from temp import temp
from music import Music
from lamp import Lamp
from time import sleep
import RPi.GPIO as GPIO

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/add')
def add():
    if 'time' not in request.args or not check_time(request.args['time']):
        return 'Error', 400
    schedule.every().day.at(request.args.get('time')).do(ring)
    return 'OK', 200


def check_time(time):
    try:
        time = time.split(':')
        if len(time) != 2 or int(time[0]) not in range(0, 24) or int(time[1]) not in range(0, 60):
            return False
    except ValueError as e:
        return False
    return True


def ring():
    print("ring")
    pass


def loop():
    while True:
        schedule.run_pending()
        lcd.update(tmp)
        if GPIO.input(12) == GPIO.LOW:
            print("next")
            music.next_song()
        time.sleep(1)

if __name__ == '__main__':
    lcd = lcd()
    tmp = temp()
    lamp = Lamp()
    lcd.update(tmp)
    sleep(5)
    music = Music()
    music.load_random()
    music.play_random()
    lamp.switch_on()
    lcd.wake_up()

    buttonPin = 12  # define the buttonPin
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    t = Thread(target=loop)
    t.start()
    app.run(host='0.0.0.0')
