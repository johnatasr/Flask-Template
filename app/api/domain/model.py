from sqlalchemy.sql import func

from app import db


class Data(db.Model):
    __tablename__ = "data"

    id = db.Column(db.Integer(), primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, server_default=func.now(), nullable=False)
