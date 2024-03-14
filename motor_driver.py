import RPi.GPIO as GPIO
from pynput import keyboard
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.HIGH)


def clean_up():
    GPIO.cleanup()

def on_press(key):
    try:
        if key.char == 't':
            clean_up()
            return False  
    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()