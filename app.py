from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1 style="color:green;">Welcome to Application Home Page</h1>'

@app.route("/info")
def sktechopsinfo():
    return '<h1 style="color:violet;">****Welcome to DevOps Project****</h1>'

@app.route("/contact")
def sktechopsemail():
    return  '<h1 style="color:red;">FOR TEST ENQUIRY: admin@domain.com</h1>'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)