from flask import Flask, request, redirect, url_for, render_template, send_file
import os
from main import main

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        result = main(file_path)  # Call the main function from main.py with the file path
        return send_file(result, as_attachment=True)  # Send the file to the user for download
    return 'File upload failed'

if __name__ == '__main__':
    app.run(debug=True)
