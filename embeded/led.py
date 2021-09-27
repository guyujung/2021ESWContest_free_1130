import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
c=0
while(c<10):
    GPIO.output(23,False)
    time.sleep(2)
    GPIO.output(23,True)
    time.sleep(2)
    c+=1
GPIO.cleanup()