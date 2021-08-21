from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    Username = db.Column(db.String(80), unique=True, nullable=False)
    Password = db.Column(db.String(120), nullable=False)
    Videos = db.relationship('Video', backref='user', lazy=True)
    Comments = db.relationship('Comment', backref='user', lazy=True)
    Description = db.Column(db.String(120), nullable=False)
    Location = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.Username

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(80), nullable=False)
    FileName = db.Column(db.String(80), nullable=False)
    DateUploaded = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    Uploader_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    Comments = db.relationship('Comment',backref='video',lazy=True)

    def __repr__(self):
        return '<Video %r>' % self.Title


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Content = db.Column(db.String(80), nullable=False)
    Commenter_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    Video_id = db.Column(db.Integer, db.ForeignKey('video.id'))

    def __repr__(self):
        return '<Comment %r>' % self.Content
