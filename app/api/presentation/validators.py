from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from flask_restx import reqparse


class BaseParser(reqparse.RequestParser):
    """Query params used to filter all items"""

    DATE_EXAMPLE = 'example: 20200330'

    def __init__(self):
        super().__init__()
        self.add_argument("after", type=str, nullable=True, help=self.DATE_EXAMPLE)
        self.add_argument("before", type=str, nullable=True, help=self.DATE_EXAMPLE)
        self.add_argument("start", type=str, nullable=True, help=self.DATE_EXAMPLE)
        self.add_argument("end", type=str, nullable=True, help=self.DATE_EXAMPLE)
        self.add_argument("url", type=str, nullable=True, help="example: www.google.com.br")
        self.add_argument("title", type=str, nullable=True, help="example: The midnight library")


@dataclass
class ParserFilters:
    """Object entity used to represent query params in a OOP way"""

    after: Optional[str] = field(default=None)
    before: Optional[str] = field(default=None)
    start: Optional[str] = field(default=None)
    end: Optional[str] = field(default=None)
    url: Optional[str] = field(default=None)
    title: Optional[str] = field(default=None)

    DEFAULT_PARAM_DATE_STR: str = "%Y%m%d"

    def after_datetime(self):
        return datetime.strptime(self.after, self.DEFAULT_PARAM_DATE_STR)

    def before_datetime(self):
        return datetime.strptime(self.before, self.DEFAULT_PARAM_DATE_STR)

    def start_datetime(self):
        return datetime.strptime(self.start, self.DEFAULT_PARAM_DATE_STR)

    def end_datetime(self):
        return datetime.strptime(self.end, self.DEFAULT_PARAM_DATE_STR)
