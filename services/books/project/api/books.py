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
