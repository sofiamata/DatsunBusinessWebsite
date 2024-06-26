# Imports
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

# My App
app = Flask(__name__)

# Main page of the application 
@app.route("/")
def index():
    return render_template("index.html")

if __name__ in "__main__":
    app.run(debug=True)