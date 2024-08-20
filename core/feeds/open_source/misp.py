import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker

from core.database import BaseModel, engine
from core.feeds.base import BaseFeed
from utils.logger import Logger


Session = sessionmaker(engine)
logger = Logger(__file__)


class MISPModel(BaseModel):
    __tablename__ = "misp"

    id = sql.Column(sql.Integer, nullable=True)
    urlhaus_reference = sql.Column(sql.String(255), nullable=True)
    url = sql.Column(sql.String(255), nullable=True)
    url_status = sql.Column(sql.String(255), nullable=True)
    host = sql.Column(sql.String(255), nullable=True)
    date_added = sql.Column(sql.DateTime, nullable=True)
    threat = sql.Column(sql.String(255), nullable=True)
    blacklists = sql.Column(sql.JSON, nullable=True)
    reporter = sql.Column(sql.String(255), nullable=True)
    larted = sql.Column(sql.String(255), nullable=True)
    tags = sql.Column(sql.JSON, nullable=True)


class MISP(BaseFeed):

    def save_to_db(self):
        total = 0

        logger.debug("Done with saving...")
        return total
