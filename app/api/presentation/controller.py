from flask_restx import Namespace, Resource

from app.api.application.data_service import DataService
from app.api.infra.exceptions import (ApiBadRequest, ApiInternalError,
                                      ApiNotFound, DataServiceException)
from app.api.infra.schema import data_fields
from app.api.presentation.validators import BaseParser

namespace = Namespace(name="", description="Main api used to represent some data")
data_parser = BaseParser()


@namespace.route("/data")
class DataView(Resource):
    """
    Api responsible for get all data items, in general could be created
    all patterns of CRUD or something like that
    """

    @namespace.expect(data_parser)
    def get(self):
        try:
            return DataService.get_all_items_with_params(
                filters=data_parser.parse_args()
            )
        except DataServiceException:
            raise ApiInternalError()
        except Exception:
            raise ApiBadRequest()


@namespace.route("/data/<string:item_id>")
class DataViewItem(Resource):
    @namespace.marshal_with(data_fields)
    def get(self, item_id: str):
        """
        Return an item by id.
        """
        item = DataService.get_item_by_id(int(item_id))

        if not item:
            raise ApiNotFound()
        return item
