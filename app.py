from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

#Create Flask instance
app = Flask(__name__)
#Create a DataBase
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campus.db'
#Secret Key
app.config['SECRET_KEY'] = 'xxboompowxx'
#Initialize the Database
db = SQLAlchemy(app)


#Models
#Teacher Model
class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    campus = db.Column(db.String(100), nullable=False, unique=True)
    #admin = db.Column(db.boolean)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create A String
    def __repr__(self):
        return '<Name %r>' % self.name

#Student Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    campus = db.Column(db.String(100), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create A String
    def __repr__(self):
        return '<Name %r>' % self.name

#Forms
class TeacherForm(FlaskForm):
    name = StringField("Enter Your Name", validators=[DataRequired()])
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField("Submit")


#Homepage
@app.route('/')
def home():
    return render_template('home.html')

#Sign up (Add new user)
@app.route('/signup')
def signup():
    name = None
    form = TeacherForm()
    return render_template('signup.html')

#Teacher Login
@app.route('/login')
def login():
    return render_template('login.html')

#Admin page
@app.route('/admin')
def admin():
    return render_template('admin.html')
#Edit Teacher

#Delete Teacher (Admin only)
@app.route('/delete/<string:id>')
def delete_teacher(id):

    return render_template('teachers.html')

#Your Students
@app.route('/yourStudents')
def yourStudents():

    return render_template('yourStudents.html')

#Add Student
@app.route('/addStudent')
def add_student():

    return render_template('addStudent.html')
#Update Student

#Delete Student
@app.route('/delete/<string:id>', methods=['GET', 'POST'])
def delete_student():

    return render_template('yourStudents.html')
#Get School Calender

#Get Your students for homepage

#Single Student Page
@app.route('/<string:name>', methods=['GET', 'POST'])
def single_student():

    return render_template('singleStudent.html')




if __name__ == "__main__":
    app.run(port=5200)