import sqlalchemy as sql
from decouple import config
from sqlalchemy.orm import sessionmaker

from core.database import BaseModel, engine
from core.feeds.base import BaseFeed
from utils.logger import Logger

logger = Logger(__name__).get_logger()

Session = sessionmaker(engine)


class XForceModel(BaseModel):
    __tablename__ = "x_force"

    url = sql.Column(sql.String(1000), nullable=True)
    created = sql.Column(sql.DateTime, nullable=True)
    date_added = sql.Column(sql.DateTime, default=sql.func.now(), nullable=True)


class XForce(BaseFeed):

    def save_to_db(self):
        total = 0
        logger.debug("Done with saving...")
        return total
