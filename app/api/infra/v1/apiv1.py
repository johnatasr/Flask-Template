from app.api.infra.routers import api_data, blueprint
from app.api.presentation.controller import namespace

api_data.add_namespace(namespace)
assert blueprint
