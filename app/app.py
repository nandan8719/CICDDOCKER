from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Azure CI/CD Pipeline build successful! This is a test application to verify the deployment process. " \
    "Congratulations on setting up your pipeline correctly!  Feel free to customize this message or add more routes to your application as needed.   This is a great starting point for your Azure CI/CD pipeline, and you can expand it with additional features or functionality as you continue to develop your application." \
    " Keep up the great work and happy coding! "

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)