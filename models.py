from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()




class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))
    profilepicture = db.Column(db.String(80))
    # dateofbirth= db.Column(db.DateTime)
    bday= db.Column(db.DateTime)
    