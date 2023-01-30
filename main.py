import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_video():
	#print(request.url)
	if 'file' not in request.files:
		flash('No file part')
		return redirect('transcription.html', filename=filename)
	file = request.files['file']
	if file.filename == '':
		flash('No video selected for uploading')
		return redirect('transcription.html' , filename=filename)
	else:
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_video filename: ' + filename)
		#flash('Video successfully uploaded and displayed below')
		return render_template('transcription.html', filename=filename)

@app.route('/display/<filename>')
def display_video(filename):
	#print('display_video filename: ' + filename)
	return redirect(url_for('transcription.html', filename='uploads/' + filename), code=301)

@app.route('/transcription')
def sample_func():
    return render_template('transcription.html')

@app.route('/transcription.html')
def func_transcription():
    return render_template('transcription.html')

@app.route('/summary.html')
def func_summary():
    return render_template('summary.html')

if __name__ == "__main__":
    app.run()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    