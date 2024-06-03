# Importing the Flask class from flask module
from flask import Flask, render_template

# let's see the content of the flask module
# print( dir(flask) )

# let's create the object of the Flask class
app = Flask(__name__)

# First route: Index route/default route
@app.route('/')
def index():
    
    # returning the response
    # return render_template('index.html')
    return render_template('index.html')

# Second route: Contact us
@app.route('/contact')
def contact():
    
    # returning the response
    return render_template('contact.html')


# Third route: About us
@app.route('/about')
def about():
    
    # returning the response
    return render_template('about.html')

# let's run the flask application
app.run(debug=True)
# app.run(debug=True, host='0.0.0.0')


