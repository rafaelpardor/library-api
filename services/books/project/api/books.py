from flask import Blueprint, json, jsonify, request
from sqlalchemy import exc

from project.api.models import Book
from project import db

books_blueprint = Blueprint('books', __name__)


@books_blueprint.route('/books/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'Success',
        'message': 'pong'
    })


@books_blueprint.route('/books/', methods=['GET'])
def get_books():
    if request.method == 'GET':
        get_books = [book.to_json() for book in Book.query.all()]
        response = {
            "origin": "api_database",
            "status": "success",
            "data": get_books
        }
        return jsonify(response), 200
