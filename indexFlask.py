from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')


def index():
    return render_template("index.html")

# Create a route decorator
@app.route('/junior_breakers')

def junior_breakers():
    return render_template("junior_breakers.html")

# Create a route decorator
@app.route('/community')

def community():
    return render_template("community.html")

# Create a route decorator
@app.route('/about')

def about():
    return render_template("about.html")