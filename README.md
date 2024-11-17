# Save The Stray Project

## Overview
An IoT and AI-powered project to detect animals on roads and provide food and water at designated feeding stations.
AI-driven and infrared cameras for detecting animals around. Whenever an animal is detected, an LED sign board on the road would be activated to alert the drivers on the road. Also as soon as the animal is detected, physical distractions (like ultrasonic sound, flash lights) would be activated to make the animal go away from the roads. The AI camera would use image processing and infrared camera would use temperature distance to detect animals. These can also be replaced by ultrasonic sensors. However, these would not be as accurate as cameras. Hence, this system makes use of cameras.
Animal feeding stations would be set up away from the road to distract the animals. These would also use ai cameras to detect animals and detect animals. These would then dispense food and water. It would also help to take care of stray animals and ensure that they lead a healthy life.
The next initiative would be to develop a website. This website would allow people to upload pictures of pets roaming on the streets or on the roads along with their locations. NGOs can then go through the animal display page to find animals in need.The NGOs would be able to search the animals based on their location The website would also contain useful blogs for animal care and also location of food dispensers and locations where deterring 


## Installation
1. Clone this repository.
2. Install dependencies:
   ```bash
   python -m pip install scikit-image scikit-learn opencv-python flask
## Running the Project
1. Run animal_detection/detect_animal.py for animal detection.
2. Run pet_feeding_station/pet_feeding.py for the feeding station. If rasberry pie not available, run pet_feeding_station/pet_feeding_simulator.py
3. Start the web app:
```bash
   cd web_app
   python app.py
