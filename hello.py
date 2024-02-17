from flask import Flask, render_template


# Create a FLask instance

app = Flask(__name__)
#Create a new route decorator

@app.route('/')

def index():
    first_name = "John"
    return render_template('index.html', first_name=first_name)
# def index():
#     return "<h1>Hall of fame</h1>"



@app.route('/user/<name>')


def user(name):
    return render_template('user.html', user_name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500