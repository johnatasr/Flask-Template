from flask_restx import fields

from app import ma
from app.api.domain.model import Data
from app.api.infra.routers import api_data


class DataSchema(ma.SQLAlchemySchema):
    """Schema used to serialize the data from database"""

    class Meta:
        model = Data

    id = ma.auto_field()
    url = ma.auto_field()
    title = ma.auto_field()
    date_added = ma.auto_field()


"""Here is a individual schema to item used for a single element"""
data_fields = api_data.model(
    "Data",
    {
        "id": fields.Integer(),
        "url": fields.String(),
        "title": fields.String(),
        "date_added": fields.DateTime(),
    },
)
