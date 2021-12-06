import json
import unittest
import datetime

from werkzeug.wrappers import response

from project import db
from project.api.models import Book
from project.tests.base import BaseTestCase


def add_book(title, subtitle, author, category, publish_date, description, created_at, updated_at, deleted_at):
    book = Book(title=title, subtitle=subtitle, author=author, category=category, publish_date=publish_date,
                description=description, created_at=created_at, updated_at=updated_at, deleted_at=deleted_at)
    db.session.add(book)
    db.session.commit()
    return book


class TestBookService(BaseTestCase):
    """Test for the Book Service."""

    def test_books_ping(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/books/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong', data['message'])
        self.assertIn('Success', data['status'])

    def test_get_books(self):
        """Ensure that get books behaves correctly"""
        add_book(title="Harry Potter 1", subtitle="el primero", author="J.K. Rowlink", category="Fantasy",
                 publish_date=datetime.datetime.today().strftime('%Y-%m-%d'), description="Es el primer libro",
                 created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(), deleted_at=None)
        
        with self.client:
            response = self.client.get('/books/')
            data = json.loads(response.data.decode())
            publish_date = data['data'][0]['publish_date']
            self.assertEqual(response.status_code, 200)
            self.assertIn('Harry Potter 1', data['data'][0]['title'])
            self.assertIn('el primero', data['data'][0]['subtitle'])
            self.assertIn('J.K. Rowlink', data['data'][0]['author'])
            self.assertIn('Fantasy', data['data'][0]['category'])
            self.assertIn(publish_date, data['data'][0]['publish_date'])
            self.assertIn('Es el primer libro', data['data'][0]['description'])
            self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()
