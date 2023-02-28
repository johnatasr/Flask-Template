from flask import Blueprint
from flask_restx import Api

"""Here we could create multiple routes and api versions"""

blueprint = Blueprint("api_data", __name__, url_prefix="/api/v1")
api_data = Api(
    blueprint,
    version="1.0",
    title="Avaaz Data API",
    description="Example of description for data API",
)
