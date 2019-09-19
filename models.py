from sqlalchemy import SQL_ALCHEMY

db = SQL_ALCHEMY()  # db객체 초기화


class userModel(db.Model):
    __tablename__ = "userModel"
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(64))
    birthdate = db.Column(db.String(64))
    name = db.Column(db.String(64))

