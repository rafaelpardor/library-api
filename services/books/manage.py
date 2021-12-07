import unittest
from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import Book

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("tests")
def run_tests():
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@cli.command("seed_db")
def seed_db():
    import datetime
    db.session.add(Book(title="Harry Potter 1", subtitle="el primero", author="J.K. Rowlink", category="Fantasy",
                        publish_date=datetime.datetime.today().strftime('%Y-%m-%d'), description="Es el primer libro"))
    db.session.add(Book(title="Harry Potter 2", subtitle="el segudno", author="J.K. Rowlink", category="Fantasy",
                        publish_date=datetime.datetime.today().strftime('%Y-%m-%d'), description="Es el segundo libro"))
    db.session.commit()


if __name__ == "__main__":
    cli()
