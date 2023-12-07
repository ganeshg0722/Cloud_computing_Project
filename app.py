from flask import Flask, request, render_template_string
from werkzeug.utils import secure_filename
import os
import script

app = Flask(__name__)

# Define the upload folder (adjust as needed)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        # if 'file' not in request.files:
        #     return render_template_string('No file part')
        
        file = request.files['file']

        # If user does not select file, browser also
        # submit an empty part without filename
        # if file.filename == '':
        #     return render_template_string('No selected file')

        if file and allowed_file(file.filename):
        #     # Save the uploaded file to the upload folder
        #     filename = secure_filename(file.filename)
        #     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        #     file.save(file_path)

            # Get user input for property ID
            user_id = int(request.form['id'])

            # Call the prediction function with user inputs
            result = script.predict_sale_price(user_id, './train.csv', './test.csv')

            return render_template_string('''
                <style>
                    body {
                        background-color: #f0f0f0;
                        text-align: center;
                        padding-top: 50px;
                    }
                    form {
                        margin: 0 auto;
                        width: 300px;
                        background-color: #ffffff;
                        padding: 20px;
                        border-radius: 10px;
                    }
                </style>
                <form method="post" enctype="multipart/form-data">
                    <input type="file" name="file" accept=".csv" required><br><br>
                    <label for="id">Enter Property ID:</label>
                    <input type="text" name="id" id="id" required><br><br>
                    <input type="submit" value="Submit">
                </form>
                {% if result %}
                    <p>Predicted Sale Price: {{ result }}</p>
                    <a href="/">Try another prediction</a>
                {% endif %}
            ''', result=result)
    
    return '''
        <style>
            body {
                background-color: #f0f0f0;
                text-align: center;
                padding-top: 50px;
            }
            form {
                margin: 0 auto;
                width: 300px;
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
            }
        </style>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file" accept=".csv" required><br><br>
            <label for="id">Enter Property ID:</label>
            <input type="text" name="id" id="id" required><br><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
