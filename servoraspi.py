import RPi.GPIO as GPIO
import time as time

def gerbang():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    servo = GPIO.PWM(18,500)
    servo.start(100)
    for dc in range(100,40,-5):
        servo.ChangeDutyCycle(dc)
        time.sleep(0.1)
        
    time.sleep(10)
        
    for dc in range(40,100,4):
        servo.ChangeDutyCycle(dc)
        time.sleep(0.1)
        
    servo.stop(100)


while True:
    gerbang()
    break
