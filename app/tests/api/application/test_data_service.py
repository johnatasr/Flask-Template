from unittest.mock import patch

import pytest
from flask_restx.reqparse import ParseResult

from app.api.application.data_service import DataService


class TestDataItemService:
    def test_get_all_items(self, items_mock):
        items = DataService.get_all_items()
        assert items
        assert type(items) == list
        assert len(items) == 10

    def test_get_all_items_with_params(self, items_mock):
        params = ParseResult(after="20000101")
        items = DataService.get_all_items_with_params(filters=params)
        assert items
        assert len(items) == 5

    @patch("app.api.domain.repository.ModelDataRepository.get_all_items_with_params")
    def test_get_all_items_with_params_data_exp(self, all_items, items_mock):
        params = ParseResult({"after": "20190101"})
        all_items.return_value = Exception()

        with pytest.raises(Exception):
            DataService.get_all_items_with_params(filters=params)

    def test_get_item_by_id(self, items_mock):
        item = DataService.get_item_by_id(1)
        assert item
        assert type(item) == dict
