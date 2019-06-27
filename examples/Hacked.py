#!/usr/bin/env python

from pycreate2 import Create2
import subprocess
import keyboard
import time

if __name__ == "__main__":
    port = '/dev/tty.usbserial-DN026E5R'
    baud = {
    	'default': 115200,
    	'alt': 19200  # shouldn't need this unless you accidentally set it to this
    }

    bot = Create2(port=port, baud=baud['default'])

    bot.start()

    bot.full()

    audio_file = "/Users/John/Documents/PythonTesting/pycreate2/examples/Ready.mp3"


    while True:
        sensor = bot.get_sensors()
        
        if sensor[0].bump_left == True:
            return_code = subprocess.call(["afplay", audio_file])
            print('found')
        elif sensor[0].bump_right == True:
            return_code = subprocess.call(["afplay", audio_file])
            print('found')


        try:
            if keyboard.is_pressed('w'):
                bot.drive_straight(450)
                time.sleep(1)
                bot.drive_stop()

        except:
            print

        try:
            if keyboard.is_pressed('a'):
                bot.turn_angle(45,150)
                time.sleep(1)
                bot.drive_stop()

        except:
            print

        try:
            if keyboard.is_pressed('s'):
                bot.drive_straight(-450)
                time.sleep(1)
                bot.drive_stop()

        except:
            print

        try:
            if keyboard.is_pressed('d'):
                bot.turn_angle(315,150)
                time.sleep(1)
                bot.drive_stop()

        except:
            print

        try:
            if keyboard.is_pressed('x'):
                exit()
        except:
            print()

        try:
            if keyboard.is_pressed('p'):
                bot.power()
        except:
            print

