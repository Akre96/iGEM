from flask import Flask, render_template, request, redirect
from werkzeug import secure_filename
import os, subprocess,time

# Initialize the Flask application
app = Flask(__name__)
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))+'/UPLOAD_FOLDER'
ALLOWED_EXTENSIONS = set(['fasta','fa'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods = [ 'POST','GET'])
def upload_file():
    if request.method == 'POST':
        # Get the FileStorage instance from request
        file = request.files['file']
	if file:
		filename =  secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'query'))
        # Render template with file info
	memory = subprocess.Popen(['python', 'script.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    	out,error = memory.communicate()
	return render_template('file.html',
		filename = filename,
		out=out,
		error=error)
    return render_template('index.html')

# Run
if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port = 4600
    )
