from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(80), nullable= False)
    email = db.Column(db.String(120), nullable= True)
    firstName = db.Column(db.String(50), nullable= False)
    lastName = db.Column(db.String(50), nullable= False)
    password_hash = db.Column(db.String(255), nullable= False)
    role = db.Column(db.String(50), nullable= True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Task(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(80), nullable= False)
    description = db.Column(db.Text, nullable= False)
    assigned_to = db.Column(db.String(50), db.ForeignKey('user.id'), nullable= True)
    status = db.Column(db.String(20), default= "Pending")
    