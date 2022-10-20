# 1. Import Flask
from flask import flask

# 2. Create an app
app = Flask(__name__)

# 3. Define index route
@app.route("/")
def index():
    return "Hello world!"
    

# 4. Define the about route
@app.route("/about")
def about():
    name = "Tyrone"
    location = "Pittsburgh"

    return f"My name is {name} and I am from {location}"

# 5. Define the contact route
@app.route("/contact")
def contact():
    email = "tyfraley81@gmail.com"
    return f"If you need help, you can email me at {email}"

# 6. Define main behavior
if __name__ = "__main__":
    app.run(debug=True)
