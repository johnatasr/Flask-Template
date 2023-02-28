from datetime import datetime

from app.api.presentation.validators import ParserFilters


class TestValidators:
    def parse_raw(self):
        return {
            "after": "20200101",
            "before": "20200101",
            "start": "20200101",
            "end": "20200101",
            "url": None,
            "title": None,
        }

    def test_crete_parse_filters(self):
        parse_raw_none = {
            "after": None,
            "before": None,
            "start": None,
            "end": None,
            "url": None,
            "title": None,
        }

        assert ParserFilters(**parse_raw_none)
        assert ParserFilters(**self.parse_raw())
        assert type(ParserFilters(**self.parse_raw())) == ParserFilters

    def test_get_all_datetime_fields(self):
        parsed_fields = ParserFilters(**self.parse_raw())
        assert type(parsed_fields.start_datetime()) == datetime
        assert type(parsed_fields.end_datetime()) == datetime
        assert type(parsed_fields.after_datetime()) == datetime
        assert type(parsed_fields.before_datetime()) == datetime
