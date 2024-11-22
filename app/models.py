from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50), nullable= False)
    role = db.Column(db.String(50), nullable= False)
    
class Task(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(80), nullable= False)
    description = db.Column(db.Text, nullable= False)
    assigned_to = db.Column(db.String(50), db.ForeignKey('user.id'), nullable= True)
    status = db.Column(db.String(20), default= "Pending")
    