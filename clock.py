from flask import Flask
import schedule
import time
from threading import Thread
from lcd import lcd
from temp import temp

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
        time.sleep(1)

if __name__ == '__main__':
    lcd = lcd()
    lcd.printWelcome()
    tmp = temp()


    t = Thread(target=loop)
    t.start()
    app.run(host='0.0.0.0')

