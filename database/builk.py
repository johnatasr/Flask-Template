import json
from typing import List, Dict
from dateutil import parser
from datetime import datetime
from app.api.domain.model import Data


def update_data(db, session=None, limit=None) -> None:
    stat = session.query(Data) if session else db.session.query(Data)
    if stat.count() == 0:
        with open("database/input/data.json") as data:
            data: Dict = json.loads(data.read())

        if "items" in data:
            data: List = data["items"]
        if limit:
            data: List = data[:limit]

        data_entries = []
        model_id = 1
        for item in data:
            date: datetime = parser.parse(item["date"])
            new_entry = Data(
                id=model_id, url=item["uri"], title=item["title"], date_added=date
            )
            data_entries.append(new_entry)
            model_id += 1

        if session:
            session.add_all(data_entries)
            session.commit()
            return
        db.session.add_all(data_entries)
        db.session.commit()
