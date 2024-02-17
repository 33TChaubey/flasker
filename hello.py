from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
# Create a FLask instance

app = Flask(__name__)
#Create a new route decorator
#Create a form class
app.config['SECRET_KEY'] = "my super secret key"
class NameForm(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
    submit = SubmitField("Submit")


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

@app.route('/name',methods=['GET','POST'])
def name():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('name.html', name=name, form=form)