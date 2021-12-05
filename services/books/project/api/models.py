from project import db

class Book(db.Model):
    __talbename__ = "book"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    subtitle = db.Column(db.String(128), nullable=False)
    author = db.Column(db.String(128), nullable=False)
    category = db.Column(db.String(128), nullable=False)
    publishDate = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    
    def __init__(self, title, subtitle):
        self.title = title
        self.subtitle = subtitle
    
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title
        }
