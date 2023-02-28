from app.api.domain.model import Data


def test_create_item(session):
    data_item = Data(title="test", url="url_test")
    session.add(data_item)
    session.commit()

    item = session.query(Data).filter_by(title="test", url="url_test").first()
    assert item.title == data_item.title
    assert item.url == data_item.url
