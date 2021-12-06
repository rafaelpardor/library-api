from project import db


class Book(db.Model):
    __talbename__ = "book"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    subtitle = db.Column(db.String(128), nullable=True)
    author = db.Column(db.String(128), nullable=False)
    category = db.Column(db.String(128), nullable=False)
    publish_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, title, subtitle, author, category, publish_date, description, created_at, updated_at, deleted_at):
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.category = category
        self.publish_date = publish_date
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

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
#     pass


# class Category(db.Model):
#     pass
