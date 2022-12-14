from flask import Flask, render_template,flash, request, redirect, url_for
import os
from coloring import changeColor

from werkzeug.utils import secure_filename
UPLOAD_FOLDER = './static/uploads/'
application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
upload=False

@application.route('/')
def home():
    filename='sofa4.jpeg'
    return render_template('index.html',filename=filename)

@application.route('/uploader',methods=['GET','POST'])
def uploader():
    global filename
    if request.method == 'POST':
        f = request.files['file1']
        upload = True
        try:
            f.save(os.path.join(application.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            filename=f.filename
        except:
            print('Invalid file')
    return render_template('index.html',filename=filename,upload=upload)

@application.route('/colorchange',methods=['POST'])
def colorchange():
     upload=False
     if request.method == 'POST':
           tfilename=request.form['tfilename']
           result=changeColor(filename,tfilename) 
           print(result)
     return render_template('index.html',filename=result,upload=upload)
 
if __name__== "__main__" :
    application.run(debug=True,port=8000)   