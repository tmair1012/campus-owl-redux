from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from datetime import datetime

#Create Flask instance
app = Flask(__name__)

#Create a DataBase
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campus.db'
#Secret Key
app.config['SECRET_KEY'] = "Evans Cybercampus sucks and they should have hired me"
#Initialize the Database
db = SQLAlchemy(app)

app.app_context().push()

#Models
class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    campus = db.Column(db.String(100), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    campus = db.Column(db.String(100), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create A String
    def __repr__(self):
        return '<Name %r>' % self.name

#Homepage
@app.route('/')
def home():
    return render_template('home.html')

#Sign up (Add new user)
@app.route('/signup')
def signup():
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

#Add Student

#Update Student

#Delete Student

#Get School Calender

#Get Your students for homepage

#Single Student Page




if __name__ == "__main__":
    app.secret_key='Shhhh'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(port=5200)