import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)

print("setup")
time.sleep(2)

for i in range(1,3):

   GPIO.output(23,True)
   print("true")
   time.sleep(2)
   GPIO.output(23,False)
   print("false")
   time.sleep(2)
GPIO.cleanup()
print("cleanup")
time.sleep(2)