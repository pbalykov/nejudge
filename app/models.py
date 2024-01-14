from app import app, db, bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(128),  unique=False, nullable=False)
    name = db.Column(db.String(64),  unique=False, nullable=False)
    
    def check_user(name):
        return User.query.filter_by(name=name).first()

    def add_user(name, login, password, repeat_password):
        if User.check_user(name) :
            return None
        if password != repeat_password :
            return None
        
        hesh_password = bcrypt.generate_password_hash(password).decode('utf-8')
        return User(name = name, login = login, password = hesh_password)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

with app.app_context():
    db.create_all()
