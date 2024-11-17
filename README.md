# Save The Stray Project

## Overview
Stray animals on the road pose risks to both road safety and their well-being. Accidents involving stray animals can result in injuries, fatalities, and vehicle damage, emphasizing the need for innovative, technology-driven solutions. This paper proposes an integrated system utilizing AI (artificial intelligence)-powered cameras, IoT (internet of things) sensors, physical deterrents, and web development. The system employs machine learning-based animal detection using HOG (histogram of oriented gradients) features extracted from images captured by infrared (IR) cameras, which are processed using a random forest classifier. The system also incorporates ultrasonic sensors and LED warning signs to deter animals and alert drivers in real time. Additionally, feeding stations are set up away from the road to distract animals and ensure their welfare. A website would allow people to upload pictures of pets roaming on the streets or on the roads along with their locations. NGOs can then go through the animal display page to find animals in need.The NGOs would be able to search the animals based on their location The website would also contain useful blogs for animal care and also location of food dispensers and locations where deterring 
The project demonstrates the potential of technology in addressing complex societal challenges and aims to create a safer coexistence between humans and stray animals. 

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
