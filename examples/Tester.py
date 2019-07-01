#!/usr/bin/env python

from breezycreate2 import Robot
import time
import pygame
import playsound


# pip install -i https://test.pypi.org/simple/ BreezyCreate2

def handle_events():
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and event.key == pygame.K_a:
                print('wa')

# Create a Create 2 -- Connect over serial
bot = Robot()


pygame.init()

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

clock = pygame.time.Clock()

#Detect keypresses and hits
while True:
    #Check for hit detections
    bumpers = bot.getBumpers()
    time.sleep(1)
    print(str(bumpers))
    if bumpers[0]:
        bot.setForwardSpeed(0)
        bot.setTurnSpeed(0)
        #playsound()
        bot.playNote('A4', 30)
    elif bumpers[1]:    
        bot.setForwardSpeed(0)
        bot.setTurnSpeed(0)
        #playsound()
        bot.playNote('A4', 60)
    #configure walls later

    #handle keypresses
    handle_events()
    

# Shut down the bot
bot.close()
