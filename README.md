Predicting House prices using google Cloud
Description
This web application is designed to predict property prices based on input from a CSV file containing property details and a specified property ID. The prediction is performed using a Random Forest model.

Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.11 installed
Docker installed
Getting Started
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/your-repository.git
cd your-repository
Build the Docker Image:

bash
Copy code
docker build -t your-image-name .
Run the Docker Container:

bash
Copy code
docker run -p 8080:8080 your-image-name
The application should now be accessible at http://localhost:8080.

Usage
Access the web application in your browser.
Upload a CSV file and enter the property ID to predict the sale price.
Configuration
Adjust the ALLOWED_EXTENSIONS variable in app.py to specify the allowed file extensions for upload.
Ensure the uploads folder exists in your project directory for file uploads.
Dependencies
Flask==2.0.1
Werkzeug==2.0.1
tensorflow_decision_forests==1.8.1
pandas==2.1.3
numpy==1.26.2
Contributing
If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are welcome.
