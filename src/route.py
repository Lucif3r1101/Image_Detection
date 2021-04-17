from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from src.convert_single_image import api
app = Flask(__name__)
app.config['UPLOAD_FOLDER']=os.path.abspath(os.path.curdir)

@app.route('/')
def upload():
    print(os.curdir)
    return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      png_path=os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
      api(png_path)
      output_file=f.filename.split(".")[0]+".html"
      #return output_file
      return render_template(output_file)
		
if __name__ == '__main__':
   app.run(debug = True)