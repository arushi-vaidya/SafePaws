# Animal Detection using Random Forest and HOG Features

This repository contains two Python scripts for animal detection using computer vision techniques. One script is for training a Random Forest classifier using HOG features from images, while the other script utilizes the trained model to perform real-time animal detection via a webcam.

## Files

1. **Training Script** (`train_model.py`): 
   - This script trains a Random Forest model to detect animals based on HOG (Histogram of Oriented Gradients) features extracted from images.
   - The trained model is saved as `random_forest_animal_classifier.pkl`.

2. **Detection Script** (`animal_detection.py`): 
   - This script loads the trained Random Forest model and uses it for real-time animal detection.
   - It captures webcam frames, extracts HOG features, and makes predictions. If an animal is detected, deterrents (LED and buzzer) are activated.

---

## Setup and Requirements

### Prerequisites

- Python 3.x
- Required Python libraries:
  - OpenCV
  - NumPy
  - Scikit-learn
  - Scikit-image
  - Joblib
  - RPi.GPIO (for Raspberry Pi GPIO control)

You can install the necessary dependencies using the following:

```bash
python -m pip install opencv-python numpy scikit-learn scikit-image joblib RPi.GPIO