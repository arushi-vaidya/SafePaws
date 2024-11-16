from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# JSON file to store image metadata
METADATA_FILE = 'uploads_metadata.json'

# Helper function to read the metadata from the JSON file
def load_metadata():
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, 'r') as f:
            return json.load(f)
    return []

# Helper function to save the metadata to the JSON file
def save_metadata(metadata):
    with open(METADATA_FILE, 'w') as f:
        json.dump(metadata, f, indent=4)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pet_blogs')
def pet_blogs():
    return render_template('pet_blogs.html')

@app.route('/feeding_stations')
def feeding_stations():
    return render_template('feeding_stations.html')

@app.route('/about')
def about():
    return render_template('about_us.html')

@app.route('/upload_picture', methods=['GET', 'POST'])
def upload_picture():
    message = None
    if request.method == 'POST':
        location = request.form.get('location')
        if not location:
            message = "Location is required"
            return render_template('upload_picture.html', message=message)
        
        if 'file' not in request.files:
            message = "No file part in the request"
            return render_template('upload_picture.html', message=message)
        
        file = request.files['file']
        if file.filename == '':
            message = "No file selected for upload"
            return render_template('upload_picture.html', message=message)
        
        if file:
            # Ensure the uploads directory exists inside static
            upload_folder = app.config['UPLOAD_FOLDER']
            os.makedirs(upload_folder, exist_ok=True)
            
            file_path = os.path.join(upload_folder, file.filename)
            file.save(file_path)

            # Load current metadata and append the new image entry
            metadata = load_metadata()
            metadata.append({"filename": file.filename, "location": location})

            # Save updated metadata back to the JSON file
            save_metadata(metadata)

            message = "Image uploaded successfully!"
    return render_template('upload_picture.html', message=message)

@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    location_filter = request.form.get('location') if request.method == 'POST' else None
    metadata = load_metadata()

    if location_filter:
        metadata = [item for item in metadata if location_filter.lower() in item['location'].lower()]

    return render_template('gallery.html', uploads=metadata, location_filter=location_filter)

@app.route('/blog/<blog_id>')
@app.route('/blog1')
def blog1():
    return render_template('blog1.html')

@app.route('/blog2')
def blog2():
    return render_template('blog2.html')

@app.route('/blog3')
def blog3():
    return render_template('blog3.html')

@app.route('/blog4')
def blog4():
    return render_template('blog4.html')

if __name__ == '__main__':
    app.run(debug=True)
