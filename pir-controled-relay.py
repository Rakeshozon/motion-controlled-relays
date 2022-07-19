import RPi.GPIO as GPIO
import time

PIR_PIN = 26
BULB_PIN = 17 # single channel relay 
FAN_PIN = 22 #single channel relay 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BULB_PIN,GPIO.OUT)
GPIO.setup(FAN_PIN,GPIO.OUT)
GPIO.setup(PIR_PIN , GPIO.IN ,pull_up_down = GPIO.PUD_DOWN)

while True:
    time.sleep(0.01)
    if(GPIO.input(PIR_PIN) == 1):
        GPIO.output(BULB_PIN,GPIO.HIGH)
        GPIO.output(FAN_PIN,GPIO.HIGH)
        print(GPIO.input(PIR_PIN))
        print ("motion detected")
        
    else:
        GPIO.output(BULB_PIN,GPIO.LOW)
        GPIO.output(BULB_PIN,GPIO.LOW)
        print(GPIO.input(PIR_PIN))
        print("motion stopped")
        
        


GPIO.cleanup()


