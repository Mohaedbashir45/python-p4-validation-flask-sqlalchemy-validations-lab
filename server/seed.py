from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
# Assuming you have defined the validation functions somewhere
# from server.validations import validate_author_name, validate_author_phone, validate_post_content, validate_post_summary, validate_post_category, validate_post_title

db = SQLAlchemy()
migrate = Migrate()

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, info={'validators': [validate_author_name]})
    phone = db.Column(db.String(10), nullable=False, info={'validators': [validate_author_phone]})
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, info={'validators': [validate_post_title]})
    content = db.Column(db.Text, nullable=False, info={'validators': [validate_post_content]})
    summary = db.Column(db.String(250), nullable=False, unique=True info={'validators': [validate_post_summary]})
    category = db.Column(db.String(20), nullable=False,  nfo={'validators': [validate_post_category]})
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
