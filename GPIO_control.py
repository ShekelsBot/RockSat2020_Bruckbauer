# Andrew Bruckbauer
# 1/8/2021
# Main Control script for timing events
# Set up to use 3 push buttons for 3 seperate events

from time import sleep
import RPi.GPIO as GPIO
import board
import subprocess
from adafruit_motorkit import MotorKit
GPIO.setmode(GPIO.BCM)

kit = MotorKit(i2c=board.I2C())
button1=18
button2=27
button3=22
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3,GPIO.IN,pull_up_down=GPIO.PUD_UP)

print ("Program Started press buttons to simulate events")
while(1):
        
        if GPIO.input(button1)==0:
                print ("Button 1 Pressed")
                print ("Arm Extension")
                kit.motor3.throttle = 1
                sleep(2)
                kit.motor3.throttle = 0
                sleep(.5)
                print ("Starting Camera Script")
                sleep (.5)
                subprocess.call("./camera_scripts/camera_control_on.sh", shell=True)
        if  GPIO.input(button2)==0:
                print ("Button 2 Pressed")
                print ("Arm Retraction")
                kit.motor3.throttle = -1
                sleep(2)
                kit.motor3.throttle = 0
                sleep(.5)
                print ("Camera data script")
                sleep(.5)
                subprocess.call("./camera_scripts/camera_control_off.sh", shell=True)
        if  GPIO.input(button3)==0:
                print ("Button 3 Pressed")
                print ("simulation shutdown event")
                sleep(.5)