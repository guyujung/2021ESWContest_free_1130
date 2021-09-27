from firebase import firebase
firebase = firebase.FirebaseApplication("https://embeded-software-default-rtdb.firebaseio.com/")

import cv2
import RPi.GPIO as GPIO
from time import sleep
import time

count=0

# set up camera object
cap = cv2.VideoCapture(0)

# QR code detection object
detector = cv2.QRCodeDetector()

# servo motor value
servoPin = 18
SERVO_MAX_DUTY = 12
SERVO_MIN_DUTY = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin,GPIO.OUT)
servo=GPIO.PWM(servoPin,50)

#led
LedPin=23
GPIO.setwarnings(False)
GPIO.setup(LedPin,GPIO.OUT)
#led2
LedPin2 = 6
GPIO.setup(LedPin2, GPIO.OUT)

#sonic
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.IN)
sonic = 0

def setServoPos(degree):
   if degree>180:
      degree=180

   duty =SERVO_MIN_DUTY +(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
   print("Degree: {} to {}(Duty)".format(degree, duty))
   servo.ChangeDutyCycle(duty)


# camera qr catch
while True:
   # sonic sensor
   GPIO.output(13,False)
   time.sleep(0.5)

   GPIO.output(13, True)
   time.sleep(0.00001)
   GPIO.output(13, False)

   while GPIO.input(19) == 0:
      start = time.time()
   while GPIO.input(19) == 1:
      end = time.time()

   time_interval = end - start
   distance = time_interval * 17000
   distance = round(distance, 2)
   #print("distance = ", distance)

   if distance < 17 :
      GPIO.output(LedPin, True)
   else :
      GPIO.output(LedPin, False)


       #get the image
   _, img = cap.read()
       #get bounding box coords and data
   data, bbox, _ = detector.detectAndDecode(img)
   servo.start(0)
       #if there is a bounding box, draw one, along with the data
   if(bbox is not None):
      for i in range(len(bbox)):
         cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255,0, 255), thickness=2)
      cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 2)

      if data:
         print("data found: ", data)

         if __name__=="__main__":
            result = firebase.get('/embeded', "abc")
            result = str(result)
            print ("result:",result)
            print ("count:",count)
            print("")

            if data == result:
               if count==0:
                  data = int(data)
                  data1 = data + 1
                                 #data = str(data)
                  firebase.put('/embeded','/abc', data1)
                  setServoPos(90)
                  GPIO.output(LedPin2,False)
                  count+=1
                  print(result)
                  print("")
                  sleep(3)

               elif count==1:
                  setServoPos(0)
                  GPIO.output(LedPin2,True)
                  count=0
                  data = int(data)
                  data1 = data-1
                  firebase.put('/embeded', '/abc', data1)
                  print(result)
                  print("")
                  sleep(3)

       # display the image preview
   cv2.imshow("code detector", img)
   if(cv2.waitKey(1) == ord("q")):
      servo.stop()
      GPIO.cleanup()
      break
# free camera object and exit
cap.release()
cv2.destroyAllWindows()


