from flask import Blueprint, jsonify, request
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


@books_blueprint.route('/books', methods=['GET'])
def get_books():
    if request.method == 'GET':
        try:
            get_books = [book.to_json() for book in Book.query.all()]
            response_object = {
                "origin": "api_database",
                "status": "success",
                "data": get_books
            }
            return jsonify(response_object), 200
        except ValueError:
            response_object = {
                "origin": "api_database",
                "status": 500,
                "message": "Failed to get books"
            }
            return response_object


@books_blueprint.route('/books/<book_id>', methods=['GET'])
def get_book_by_id(book_id):
    try:
        get_book = Book.query.filter_by(id=int(book_id)).first()

        if not get_book:
            response_object = {
                "origin": "api_database",
            }
            response_object['message'] = "Book not found"
            response_object['status'] = 404
            response_object['data'] = []
            return jsonify(response_object), 404

        response_object = {
            "origin": "api_database",
            "status": 200,
            "data": {
                "id": get_book.id,
                "title": get_book.title
            }
        }
        return jsonify(response_object), 200
    except ValueError:
        response_object = {
            "origin": "api_database",
            "status": 500,
            "message": "Failed to get book"
        }
        return jsonify(response_object), 500


@books_blueprint.route('/books/byany', methods=['GET'])
def get_book_by_parameter():
    try:
        parameter = str(list(dict(request.args).keys())[0])
        search = request.args.get(parameter)
        search_book = db.session.query(Book).filter(
            getattr(Book, parameter).ilike("%" + search + "%")
        )
        format_books = [book.to_json() for book in search_book]

        if not search_book:
            response_object = {
                "origin": "api_database",
            }
            response_object['message'] = "Book not found"
            response_object['status'] = 404
            response_object['data'] = []
            return jsonify(response_object), 404

        response_object = {
            "origin": "api_database",
            "status": 200,
            "data": format_books
        }
        return jsonify(response_object), 200
    except TypeError:
        response_object = {
            "origin": "api_database",
            "status": 500,
            "message": "Failed to get book"
        }
        return jsonify(response_object), 500


@books_blueprint.route('/books/', methods=['POST'])
def create_book():
    if request.method == 'POST':
        pass


@books_blueprint.route('/books/<id>', methods=['PUT'])
def update_book():
    pass


@books_blueprint.route('/books/books', methods=['GET'])
def delete_book():
    pass
