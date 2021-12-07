import datetime

from project import db


class Book(db.Model):
    __talbename__ = "book"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    subtitle = db.Column(db.String(128), nullable=True)
    author = db.Column(db.String(128), nullable=False)
    category = db.Column(db.String(128), nullable=False)
    publish_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    deleted_at = db.Column(db.DateTime, nullable=True, default=None)

    def __init__(self, title, author, category, publish_date):
        self.title = title
        self.author = author
        self.category = category
        self.publish_date = publish_date

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'subtitle': self.subtitle,
            'author': self.author,
            'category': self.category,
            'publish_date': self.publish_date,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'deleted_at': self.deleted_at,
        }


# class Author(db.Model):
#     __tablename__ = "author"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(128), nullable=False)


# class Category(db.Model):
#     pass
