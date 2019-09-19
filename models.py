from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # db객체생성


class userModel(db.Model):
    __tablename__ = "user_DB"
    id = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(64))
    birthdate = db.Column(db.Integer)
    name = db.Column(db.String(64))
