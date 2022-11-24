from flask import Flask, render_template,flash, request, redirect, url_for
import os
from hue_changer import colorChanger

from werkzeug.utils import secure_filename
UPLOAD_FOLDER = '/Users/sugunapriya/python_projects/image_processing/static/uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
upload=False

@app.route('/')
def home():
    filename='bluesofa.jpg'
    return render_template('index.html',filename=filename)

@app.route('/uploader',methods=['GET','POST'])
def uploader():
    global filename
    if request.method == 'POST':
        f = request.files['file1']
        upload = True
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        filename=f.filename
    return render_template('index.html',filename=filename,upload=upload)

@app.route('/colorchange',methods=['POST'])
def colorchange():
     upload=False
     if request.method == 'POST':
           tfilename=request.form['tfilename']
           result=colorChanger(filename,tfilename) 
         
     return render_template('index.html',filename=result,upload=upload)
 
if __name__== "__main__" :
    app.run(debug=True,port=8000)   