import RPi.GPIO as GPIO
import time

PIR_PIN = 26
LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN ,GPIO.OUT)
GPIO.setup(PIR_PIN , GPIO.IN ,pull_up_down = GPIO.PUD_DOWN)

while True:
    time.sleep(0.01)
    if(GPIO.input(PIR_PIN) == 1):
        GPIO.output(LED_PIN,GPIO.HIGH)
        print(GPIO.input(PIR_PIN))
        
    else:
        GPIO.output(LED_PIN,GPIO.LOW)
        print(GPIO.input(PIR_PIN))
        
        


GPIO.cleanup()
