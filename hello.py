from flask import Flask
app = Flask(__name__)
# print(__name__)

#Decorators to add a tag around text on web page.
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper()


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello World! </h1>'\
            '<p>Hi there.</p>'\
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHRycDh5ZHhtbDRlYWE3d2toN3M2OWttOTh4Nm4yYzBtNDJ3NmxmbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Cmr1OMJ2FN0B2/giphy.gif" width= 500px>'



# @-- python decorator
#Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"


# creating variable path and converting the path to a specific data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}! You are {number} years old"

if __name__ == "__main__":
    app.run(debug=True) #auto-reloads when you save changes
