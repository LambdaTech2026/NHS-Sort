from flask import Flask, request, redirect, url_for, render_template, send_file, Response
import os
import csv
import openpyxl
import smtplib
from main import main
from excel import emain
global filePathGlobal, teachers_emailed, current_teacher, students, xl
filePathGlobal = False
current_teacher = None
teachers_emailed = set()
students = []
xl = None

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global filePathGlobal
    if request.files['file'].filename != 'email_test.csv':
        result = down()
    else:
        filePathGlobal = True
        print(filePathGlobal)
    return redirect(url_for('downloaded'))

def down():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        result = main(file_path)
        return send_file(result, as_attachment=True)  # Send the file to the user for download
    return 'File upload failed'

@app.route("/downloaded")
def downloaded():
    return render_template("downloaded.html")

@app.route("/getPlotCSV")
def getPlotCSV():
    
    with open("FORMATTED.csv") as fp:
        csv = fp.read()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=FORMATTED.csv"})


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/teach', methods=['POST'])
def teach():
    global xl
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        xl = file_path
        result = emain(file_path)
        return redirect(url_for('formdown'))

@app.route("/getxlsx")
def getxlsx():
    return send_file(
        xl,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True, 
    )

@app.route("/formdown.html")
def formdown():
    return render_template('formdown.html')


if __name__ == '__main__':
    app.run(debug=True)
