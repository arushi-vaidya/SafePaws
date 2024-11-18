import cv2
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from skimage.feature import hog
from skimage import exposure
from sklearn.preprocessing import LabelEncoder
import os
import joblib

# Define function to extract HOG features from an image
def extract_hog_features(image):
    fd, hog_image = hog(image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True, channel_axis=-1)
    return fd

# Load dataset
def load_dataset(dataset_path):
    features = []
    labels = []
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset path {dataset_path} does not exist.")
        return np.array(features), np.array(labels)
    for folder in os.listdir(dataset_path):
        folder_path = os.path.join(dataset_path, folder)
        if os.path.isdir(folder_path):
            for image_name in os.listdir(folder_path):
                image_path = os.path.join(folder_path, image_name)
                image = cv2.imread(image_path)
                if image is None:
                    print(f"Warning: {image_path} could not be loaded, skipping.")
                    continue
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = cv2.resize(image, (224, 224))
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

# Create and train the Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train_encoded)

# Predict on the validation data
y_pred = clf.predict(X_val)

# Evaluate the model
accuracy = accuracy_score(y_val_encoded, y_pred)
print(f"Validation Accuracy: {accuracy * 100:.2f}%")

# Save the trained model
joblib.dump(clf, 'random_forest_animal_classifier.pkl')
print("Model saved as random_forest_animal_classifier.pkl")
