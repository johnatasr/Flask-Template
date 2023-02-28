from flask_sqlalchemy import BaseQuery

from app.api.domain.model import Data
from app.api.domain.repository import ModelDataRepository


class TestDataItemRepository:
    def test_get_item_by_id(self, items_mock):
        item: Data = ModelDataRepository.get_item_by_id(1)
        assert item
        assert type(item.url) == str == type(item.title)

    def test_get_all_items(self, items_mock):
        items: BaseQuery = ModelDataRepository.get_all_items()
        assert items
        assert len(items) == 10

    def test_get_all_items_with_params(self, items_mock):
        items: BaseQuery = ModelDataRepository.get_all_items_with_params(
            [Data.title.contains("mo")]
        )
        assert items
        assert items.count() == 2
