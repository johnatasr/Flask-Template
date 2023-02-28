from unittest.mock import patch

from dateutil.parser import parse
from flask.testing import FlaskClient
from flask.wrappers import Response
from flask_restx import marshal
from sqlalchemy.orm.scoping import ScopedSession

from app.api.application.data_service import DataService
from app.api.infra.exceptions import DataServiceException
from app.api.infra.schema import data_fields

API_ROOT = "api/v1/data"


class TestIDataItems:
    def item(self) -> dict:
        item = (
            {
                "id": 4,
                "title": "A possibilidade de conseguir naturalmente",
                "url": "http://www.brown-mcdonald.com/",
                "date_added": parse("06 Oct 1980"),
            },
        )
        return marshal(item, data_fields)

    def test_get_all(self, client: FlaskClient, session: ScopedSession, items_mock):
        with client:
            response: Response = client.get(API_ROOT)
        assert response.status_code == 200

    def test_get_all_filter_by_url(
        self, client: FlaskClient, session: ScopedSession, items_mock
    ):
        with client:
            response: Response = client.get(API_ROOT + "?url=brown-mcdonald")
        assert response.status_code == 200
        assert response.json == self.item()

    def test_get_all_filter_by_title(
        self, client: FlaskClient, session: ScopedSession, items_mock
    ):
        with client:
            response: Response = client.get(
                API_ROOT + "?title=possibilidade de conseguir natur"
            )
        assert response.status_code == 200
        assert response.json == self.item()

    def test_get_all_filter_by_before(
        self, client: FlaskClient, session: ScopedSession, items_mock
    ):
        with client:
            response: Response = client.get(API_ROOT + "?before=20200101")
        assert response.status_code == 200
        assert len(response.json) == 10

    def test_get_all_filter_by_after(
        self, client: FlaskClient, session: ScopedSession, items_mock
    ):
        with client:
            response: Response = client.get(API_ROOT + "?after=19900101")
        assert response.status_code == 200
        assert len(response.json) == 6

    def test_get_all_filter_by_range(
        self, client: FlaskClient, session: ScopedSession, items_mock
    ):
        with client:
            response: Response = client.get(API_ROOT + "?start=20000101&end=20200101")
        assert response.status_code == 200
        assert len(response.json) == 5

    @patch.object(DataService, "get_all_items_with_params", return_value={})
    def test_get_all_empty(
        self,
        data_service: DataService,
        client: FlaskClient,
        session: ScopedSession,
        items_mock,
    ):
        with client:
            response: Response = client.get(API_ROOT)
        assert response.status_code == 200
        assert len(response.json) == 0

    @patch("app.api.presentation.controller.DataService.get_all_items_with_params")
    def test_get_all_with_repository_exception(
        self, get_items: object, client: FlaskClient, session: ScopedSession, items_mock
    ):
        get_items.side_effect = DataServiceException()
        with client:
            response: Response = client.get(API_ROOT)
        assert response.status_code == 500
        assert (
            response.json.get("message")
            == "The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application."
        )

    @patch("app.api.presentation.controller.DataService.get_all_items_with_params")
    def test_get_all_with_exception(
        self, get_items: object, client: FlaskClient, session: ScopedSession, items_mock
    ):
        get_items.side_effect = Exception()
        with client:
            response: Response = client.get(API_ROOT)
        assert response.status_code == 400
        assert (
            response.json.get("message")
            == "The browser (or proxy) sent a request that this server could not understand."
        )


class TestIDataItem:
    def test_get_item_by_id(
        self, client: FlaskClient, session: ScopedSession, items_mock
    ):
        with client:
            response: Response = client.get(API_ROOT + "/1")
        assert response.status_code == 200

    @patch("app.api.presentation.controller.DataService.get_item_by_id")
    def test_get_item_by_id_empty(
        self, get_items: object, client: FlaskClient, session: ScopedSession, items_mock
    ):
        get_items.return_value = None
        with client:
            response: Response = client.get(API_ROOT + "/1")
        assert response.status_code == 404

    @patch("app.api.presentation.controller.DataService.get_item_by_id")
    def test_get_item_by_id_exception(
        self, get_items: object, client: FlaskClient, session: ScopedSession, items_mock
    ):
        get_items.side_effect = Exception()
        with client:
            response: Response = client.get(API_ROOT + "/1")
        assert response.status_code == 500
