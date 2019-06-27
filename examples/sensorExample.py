#!/usr/bin/env python
# ----------------------------------------------------------------------------
# MIT License
# shows how to get sensor data from the create 2

from __future__ import print_function
from pycreate2 import Create2
import subprocess
import os
import time


if __name__ == "__main__":
	port = '/dev/tty.usbserial-DN026E5R'
	baud = {
		'default': 115200,
		'alt': 19200  # shouldn't need this unless you accidentally set it to this
	}

	bot = Create2(port=port, baud=baud['default'])

	bot.start()

	bot.safe()

        audio_file = "/Users/John/Documents/PythonTesting/pycreate2/examples/Ready.mp3"

	print('Starting ...')

	while True:
		# Packet 100 contains all sensor data.
		sensor = bot.get_sensors()

		print('==============Updated Sensors==============')
                print("Bumps and wheeldrops: " + str(sensor[0]))
                print(sensor[0])
                print(sensor[0].bump_left)
                print(sensor[0].bump_right)

                if sensor[0].bump_left == True:
                   return_code = subprocess.call(["afplay", audio_file])
                elif sensor[0].bump_right == True:
                    return_code = subprocess.call(["afplay", audio_file])

                time.sleep(1)
