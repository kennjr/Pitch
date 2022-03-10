
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager
from app.main import main


class User(db.Model, UserMixin):
    # __tablename__ variable allows us to give the tables in our database proper names.
    # If not used SQLAlchemy will assume that the tablename is the lowercase of the class name.
    __tablename__ = 'users'
    # By default the Column class has primary_key set to False.
    # We want to set it to True on the id column to set it as the primary_key column.
    # Integer specifies the data in that column should be an Integer.
    id = db.Column(db.Integer, primary_key=True)
    # We create columns using the db.Column class which will represent a single column.
    # We pass in the type of the data to be stored as the first argument. db.
    # The db.String class specifies the data in that column should be a string with a maximum of 255 characters.
    username = db.Column(db.String(255))

    email = db.Column(db.String(255), unique=True, index=True)
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    photos = db.relationship('Photo', backref='photo', lazy="dynamic")

    # We use the @property decorator to create a write only class property password.
    @property
    # When we set this property we generate a password hash and pass the hashed password,
    #  as a value to the pass_secure column property to save to the database.
    def password(self):
        # We raise an AttributeError to block access to the password property.
        # This is because it is not secure for Users to have access to that property.
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    # We create a method verify_password that takes in a password,
    #  hashes it and compares it to the hashed password to check if they are the same.
    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def is_active(self):
        return True

    # Flask-login has a decorator @login_manage.user_loader that modifies the load_userfunction,
    #  by passing in a user_id to the function that queries the database and gets a User with that ID.
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # The __repr__method is not really important. It makes it easier to debug our applications.
    def __repr__(self):
        return f'User {self.username}'


class Photo(db.Model):
    __tablename__ = "photos"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    type = db.Column(db.String(255))
    photo_url = db.Column(db.String)

    def __repr__(self):
        return f'Photo {self.type}'


class Pitch(db.Model):
    __tablename__ = "pitches"

    id = db.Column(db.Integer, primary_key=True)
    pitch_txt = db.Column(db.String)

    creator_id = db.Column(db.Integer)
    upvt = db.Column(db.String)
    dwnvt = db.Column(db.String)
    timestamp = db.Column(db.String(255))
    comments = db.Column(db.String)

    def __repr__(self):
        return f'Pitch {self.pitch_txt}'

