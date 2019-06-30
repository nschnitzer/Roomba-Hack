#!/usr/bin/env python

from breezycreate2 import Robot
import time


# pip install -i https://test.pypi.org/simple/ BreezyCreate2


# Create a Create 2 -- Connect over serial
bot = Robot()

# Play a note
bot.playNote('A4', 100)

# Turn Right Slowly
bot.setTurnSpeed(-50)

# Wait a sec
time.sleep(1)

# Stop the robot
bot.setTurnSpeed(0)

# Report bumper hits and wall proximity for 30 sec
start_time = time.time()
while (time.time() - start_time) < 30:
    print('Bumpers" ' + str(bot.getBumpers()) + '   Wall: ' + str(bot.getWallSensor()))


# Shut down the bot
bot.close()
