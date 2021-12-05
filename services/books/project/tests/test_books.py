import json
import unittest

from project import db
from project.api.models import Book
from project.tests.base import BaseTestCase


class TestBookService(BaseTestCase):
    """Test for the Book Service."""

    def test_books_ping(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/books/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong', data['message'])
        self.assertIn('Success', data['status'])


if __name__ == '__main__':
    unittest.main()
