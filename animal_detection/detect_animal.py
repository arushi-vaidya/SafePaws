import cv2
import numpy as np
import RPi.GPIO as GPIO
import time
import joblib
from skimage.feature import hog
from skimage import exposure
from RPLCD.i2c import CharLCD  # Import LCD library

# Load the trained Random Forest model
rf_model = joblib.load('random_forest_animal_classifier.pkl')

# Setup GPIO for deterrents
LED_PIN = 18
BUZZER_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Setup I2C LCD
lcd = CharLCD('PCF8574', 0x27)  # Change '0x27' if your LCD has a different I2C address

def activate_deterrents():
    GPIO.output(LED_PIN, GPIO.HIGH)
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    lcd.clear()
    lcd.write_string("Animal Detected!")
    lcd.cursor_pos = (1, 0)  # Move to the second line
    lcd.write_string("Go Slow")
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    lcd.clear()

# Define function to extract HOG features from an image
def extract_hog_features(image):
    fd, hog_image = hog(image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True, channel_axis=-1)
    hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))
    return fd

# Function to detect animal using the Random Forest model
def detect_animal(frame):
    resized_frame = cv2.resize(frame, (224, 224))  # Resize to match model's input size
    hog_features = extract_hog_features(resized_frame)  # Extract HOG features
    prediction = rf_model.predict([hog_features])  # Predict using the Random Forest model
    return prediction[0] == 1  # Returns True if an animal is detected (assuming '1' means animal detected)

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
    lcd.clear()
    print("Program terminated.")
