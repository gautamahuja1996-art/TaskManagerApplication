# Importing the Flask class from flask module
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# let's see the content of the flask module
# print( dir(flask) )

# let's create the object of the Flask class
app = Flask(__name__)






# connecting the flask app (server) with sqllite database
# let's write the url: This command tells the flask app to connect with a sqllite type database named task.db
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'


# creating an object of SQLalchemy class
# Telling the SQLAlchemy class, which flask app to connect with
database = SQLAlchemy(app)




# writing python class which will be used to insert data into table
class Task(database.Model):

    sno = database.Column(database.Integer, primary_key= True)
    taskTitle = database.Column(database.String(100), nullable= False)
    taskDescription = database.Column(database.String(200), nullable= False)







# First route: Index route/default route
@app.route('/', methods = ["GET", "POST"])
def index():

    # print(request.form)

    # let's check if the request is get or post
    # if request is post --> 
    if request.method == "POST":
        
        # fetch the values of title and description
        task_title = request.form.get('title')
        task_description = request.form.get('description')
        print(task_title, task_description)

        # add it to the database
        task = Task(taskTitle= task_title, taskDescription= task_description)
        database.session.add(task)
        database.session.commit()

    

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
if __name__ == "__main__":
    app.run(debug=True)
# app.run(debug=True, host='0.0.0.0')


