from app import db

class User_model(db.Model):
    user_id = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    username = db.Column(db.String(32))

    def add_user(self):
        db.session.add(self)
        db.session.commit()