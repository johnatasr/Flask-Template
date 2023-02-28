import pytest

from app import create_app
from app import db as _db
from database.builk import update_data


@pytest.fixture(scope="session")
def app():
    """
    Returns session-wide application.
    """
    return create_app("testing")


@pytest.fixture(scope="session")
def client(app):
    """
    Return session-wide client.
    """
    return app.test_client()


@pytest.fixture(scope="session")
def db(app):
    """
    Returns session-wide initialised database.
    """
    with app.app_context():
        _db.drop_all()
        _db.create_all()


@pytest.fixture(scope="function", autouse=True)
def session(app, db):
    """
    Returns function-scoped session.
    """
    with app.app_context():
        conn = _db.engine.connect()
        txn = conn.begin()

        options = dict(bind=conn, binds={})
        sess = _db.create_scoped_session(options=options)

        _db.session = sess

        yield sess

        sess.remove()
        txn.rollback()
        conn.close()


@pytest.fixture
def items_mock(app, session, db):
    with app.app_context():
        update_data(db, session=session, limit=10)
    yield
