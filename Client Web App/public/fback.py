import os
from flask import Flask, request, redirect, url_for, send_from_directory,render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Users/japneetkaursaluja/Desktop/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

#app = Flask(__name__, template_folder='../pages/templates')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = str(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #return redirect(url_for('uploaded_file', filename=filename))
            return "Successfully Uploaded"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method="post" enctype="multipart/form-data">
      <p><input type="file" name="file">
         <input type="submit" value="Upload">
    </form>
    '''

#@app.route('/uploads/<filename>', methods=['GET'])
#def uploaded_file(filename):
#   new_filename =  + filename
#   return render_template('template.html', filename = new_filename)

if __name__ == '__main__':
    app.run()
