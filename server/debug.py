from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates, Session
from . import db

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    phone_number = Column(String)

    @validates('phone_number')
    def validate_phone_number(self, key, value):
        if value is not None:
            if not value.isdigit() or len(value) != 10:
                raise ValueError("Phone number must be exactly ten digits.")
        return value

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)
    summary = Column(String)
    category = Column(String)

    @validates('title')
    def validate_title(self, key, value):
        clickbait_phrases = ["amazing secrets", "they don't want you to know"]
        for phrase in clickbait_phrases:
            if phrase in value.lower():
                raise ValueError("Title is clickbait.")
        return value

    @validates('content')
    def validate_content_length(self, key, value):
        if value is not None and len(value) < 250:
            raise ValueError("Content must be at least 250 characters long.")
        return value

    @validates('summary')
    def validate_summary_length(self, key, value):
        if value is not None and len(value) > 250:
            raise ValueError("Summary cannot exceed 250 characters.")
        return value

    @validates('category')
    def validate_category(self, key, value):
        if value not in ['Fiction', 'Non-Fiction']:
            raise ValueError("Category must be either 'Fiction' or 'Non-Fiction'.")
        return value

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title}, content={self.content}, summary={self.summary})'