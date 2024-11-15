from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

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
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            return redirect(url_for('home'))
    return render_template('upload_picture.html')

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
