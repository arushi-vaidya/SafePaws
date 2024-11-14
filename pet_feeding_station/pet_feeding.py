import RPi.GPIO as GPIO
import time

PIR_SENSOR_PIN = 17
DISPENSER_PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_SENSOR_PIN, GPIO.IN)
GPIO.setup(DISPENSER_PIN, GPIO.OUT)

def activate_dispenser():
    GPIO.output(DISPENSER_PIN, GPIO.HIGH)
    time.sleep(5)  
    GPIO.output(DISPENSER_PIN, GPIO.LOW)

try:
    while True:
        if GPIO.input(PIR_SENSOR_PIN):
            print("Animal detected at feeding station!")
            activate_dispenser()
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Feeding station deactivated.")
