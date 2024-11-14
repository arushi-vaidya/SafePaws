import cv2
import tensorflow as tf
import RPi.GPIO as GPIO
import time

# Load pre-trained model
model = tf.keras.models.load_model('animal_detection_model.h5')

# Setup GPIO for deterrents
LED_PIN = 18
BUZZER_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

def activate_deterrents():
    GPIO.output(LED_PIN, GPIO.HIGH)
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

def detect_animal(frame):
    resized_frame = cv2.resize(frame, (224, 224)) / 255.0
    prediction = model.predict(tf.expand_dims(resized_frame, axis=0))
    return prediction[0][0] > 0.5  # True if an animal is detected

cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if ret and detect_animal(frame):
            print("Animal detected!")
            activate_deterrents()
        time.sleep(0.5)
except KeyboardInterrupt:
    cap.release()
    GPIO.cleanup()
    print("Program terminated.")
