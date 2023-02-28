from typing import Dict, List

from flask_restx.reqparse import ParseResult
from flask_sqlalchemy import BaseQuery

from app.api.domain.model import Data
from app.api.domain.repository import ModelDataRepository
from app.api.infra.exceptions import DataServiceException
from app.api.infra.schema import DataSchema
from app.api.presentation.validators import ParserFilters

data_item_schema = DataSchema()
data_items_schema = DataSchema(many=True)


class DataService:
    """
    Layer responsible for some use cases and business rules, could be used to avoid
    excessive code in controller also used as intermediary for repositories
    """

    ALLOWED_SEARCH_FIELDS = ["url", "title"]

    @classmethod
    def get_all_items(cls) -> List:
        """Get all items without filters"""
        all_items: BaseQuery = ModelDataRepository.get_all_items()
        return data_items_schema.dump(all_items)

    @classmethod
    def get_all_items_with_params(cls, filters: ParseResult) -> List:
        """Get all items with parsed filters, filters must be allowed in ALLOWED_SEARCH_FIELDS
        to match with model filters
        """
        parser = ParserFilters(**filters)
        custom_filter = []

        if parser.after:
            custom_filter = [Data.date_added > parser.after_datetime()]
        elif parser.before:
            custom_filter = [Data.date_added < parser.before_datetime()]
        elif parser.start and parser.end:
            custom_filter = [
                Data.date_added >= parser.start_datetime(),
                Data.date_added <= parser.end_datetime(),
            ]
        for field in cls.ALLOWED_SEARCH_FIELDS:
            if getattr(parser, field):
                custom_filter.append(getattr(Data, field).contains(filters[field]))

        try:
            all_items: BaseQuery = ModelDataRepository.get_all_items_with_params(
                custom_filter
            )
        except Exception:
            raise DataServiceException("Error when tried get all items with filters")

        return data_items_schema.dump(all_items)

    @classmethod
    def get_item_by_id(cls, item_id: int) -> Dict:
        """Get item by id, here we could put some business rules and maintain clean our structure"""
        data_item: Data = ModelDataRepository.get_item_by_id(item_id)
        return data_item_schema.dump(data_item)
