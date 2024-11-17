import cv2
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from skimage.feature import hog
from skimage import exposure
from sklearn.preprocessing import LabelEncoder
import os
import joblib

# Define function to extract HOG features from an image
def extract_hog_features(image):
    fd, hog_image = hog(image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True, channel_axis=-1)
    hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))
    return fd

# Load dataset
def load_dataset(dataset_path):
    features = []
    labels = []
    for folder in os.listdir(dataset_path):
        folder_path = os.path.join(dataset_path, folder)
        if os.path.isdir(folder_path):
            for image_name in os.listdir(folder_path):
                image_path = os.path.join(folder_path, image_name)
                image = cv2.imread(image_path)

                # Check if image is loaded correctly
                if image is None:
                    print(f"Warning: {image_path} could not be loaded, skipping.")
                    continue  # Skip this image

                image = cv2.resize(image, (224, 224))  # Resize to a consistent size
                hog_features = extract_hog_features(image)
                features.append(hog_features)
                labels.append(folder)
    
    return np.array(features), np.array(labels)

# Load data
train_path = 'dataset/train'
val_path = 'dataset/validation'
X_train, y_train = load_dataset(train_path)
X_val, y_val = load_dataset(val_path)

# Encode labels as integers
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_val_encoded = label_encoder.transform(y_val)

# Split data into training and validation sets
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train_encoded, test_size=0.2, random_state=42)

# Create and train the Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict on the validation data
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Validation Accuracy: {accuracy * 100:.2f}%")

# Save the trained model (optional)
joblib.dump(clf, 'random_forest_animal_classifier.pkl')
print("Model saved as random_forest_animal_classifier.pkl")
