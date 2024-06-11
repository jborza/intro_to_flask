from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SECRET_KEY'] = 'c41b428eee11a1fe001808ed3d3fa29ed2a23f7175552395'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    is_completed = db.Column(db.Boolean, default=False)
    done = db.Column(db.Boolean, default=False)

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(min=1, max=100)])
    description = TextAreaField('Description', validators=[Length(max=200)])
    is_complete = BooleanField('Is Completed')
    submit = SubmitField('Submit')

@app.route('/task', methods=['GET', 'POST'])
def task():
    form = TaskForm()
    if form.validate_on_submit():
        return redirect(url_for('hello_world'))
    return render_template('task.html', form=form)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def user(username):
    return 'User %s' % username

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/users')
def users():
    user_names = ['Alice', 'Bob', 'Charlie']
    return render_template('users.html', names=user_names)