from app import app, db, bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(128),  unique=False, nullable=False)
    name = db.Column(db.String(64),  unique=False, nullable=False)
    
    def add_user(name, login, password, repeat_password):
        if User.query.filter_by(login=login).first():
            return None
        if password != repeat_password :
            return None       
        hesh_password = bcrypt.generate_password_hash(password).decode('utf-8')
        return User(name = name, login = login, password = hesh_password)

    def get_user(login, password):
        user = User.query.filter_by(login=login).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return True
        return False

    def __repr__(self):
        return '<User %r>' % (self.nickname)

with app.app_context():
    db.create_all()
