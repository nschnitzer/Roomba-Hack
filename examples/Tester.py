#!/usr/bin/env python

from breezycreate2 import Robot
import time
import pygame
import playsound


# pip install -i https://test.pypi.org/simple/ BreezyCreate2

def handle_events():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w and event.key == pygame.K_a:
            print('wa')

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
#start_time = time.time()
#while (time.time() - start_time) < 30:
#    print('Bumpers" ' + str(bot.getBumpers()) + '   Wall: ' + str(bot.getWallSensor()))


#Detect keypresses and hits
while True:
    #Check for hit detections
    bumpers = bot.getBumpers()
    if bumpers[0]:
        bot.stop()
        playsound()
        bot.start()
    elif bumpers[1]:
        bot.stop()
        playsound()
        bot.start()
    #configure walls later

    #handle keypresses
    handle_events()
    

# Shut down the bot
bot.close()
