import RPi.GPIO as GPIO
import time

print("start")

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.IN)

try:
   while True:
      GPIO.output(13, False)
      time.sleep(0.5)

      GPIO.output(13, True)
      time.sleep(0.00001)
      GPIO.output(13, False)

      while GPIO.input(19) == 0:
         start = time.time()

      while GPIO.input(19) == 1 :
         stop = time.time()

      time_interval = stop - start
      distance = time_interval * 17000
      distance = round(distance, 2)

      print("distance = ", distance, "cm")

except KeyboardInterrupt:
   GPIO.cleanup()
   print("end")
