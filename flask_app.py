from flask import Flask, render_template, request, redirect, Markup
from werkzeug import secure_filename
import os, subprocess,time

# Initialize the Flask application
app = Flask(__name__)
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))+'/UPLOAD_FOLDER/'
ALLOWED_EXTENSIONS = set(['fasta','fa'])
scriptPath = os.path.dirname(os.path.abspath(__file__))+'/script.py'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods = [ 'POST','GET'])
def upload_file():
    if request.method == 'POST':
        # Get the FileStorage instance from request
        if request.files['file']:
            file = request.files['file']
            filename =  secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'query'))
            with open(os.path.join(app.config['UPLOAD_FOLDER'], 'query'),'r') as f:
                fileData = f.readlines();
            mode='1';

        # Render template with file info            
        else:
            filename = 'SampleData'
            mode='0'
            with open(os.path.dirname(os.path.abspath(__file__))+'/query.fa') as f:
                fileData = f.readlines();

        for line in fileData:
            line = line.replace('/n','<br/>')
        
        

	memory = subprocess.Popen(['python', scriptPath,mode],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    	out,error = memory.communicate()
	return render_template('file.html',
		filename = filename,
        fileData= fileData,
		out= Markup(out),
		error= error)
    return render_template('index.html')

# Run

if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port = 4600,
        debug=True
    )
