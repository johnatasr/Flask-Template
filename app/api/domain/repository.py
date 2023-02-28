from flask_sqlalchemy import BaseQuery

from app import db
from app.api.domain.model import Data


class ModelDataRepository(object):
    """
    Layer responsible to connect use-case/services with Models, could be similar to DTO but the main reason is
    avoid model calls through the code structure
    """

    @classmethod
    def get_item_by_id(cls, item_id: int) -> Data:
        return db.session.query(Data).filter_by(id=item_id).first()

    @classmethod
    def get_all_items(cls) -> BaseQuery:
        return db.session.query(Data).all()

    @classmethod
    def get_all_items_with_params(cls, custom_filters: list) -> BaseQuery:
        return db.session.query(Data).filter(*custom_filters)
