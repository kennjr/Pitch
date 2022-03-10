from app import db


class User(db.Model):
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
    photos = db.relationship('Photo', backref='photo_url', lazy="dynamic")


class Photo(db.Model):
    __tableanme__ = "photos"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    type = db.Column(db.String(255))
    photo_url = db.Column(db.String)

    def __repr__(self):
        return f'Photo {self.type}'

