import sqlalchemy as sql
from decouple import config
from sqlalchemy.orm import sessionmaker
from requests.auth import HTTPBasicAuth
import requests
from core.database import BaseModel, engine
from core.feeds.base import BaseFeed
from utils.logger import Logger

logger = Logger(__name__).get_logger()
X_FORCE__URL = "https://api.xforce.ibmcloud.com/api/url?category=Malware"

Session = sessionmaker(engine)


class DarkTraceModel(BaseModel):
    __tablename__ = "darktrace"

    CVE = sql.Column(sql.String(1000), nullable=True)
    Name = sql.Column(sql.String(1000), nullable=True)
    Severity = sql.Column(sql.String(1000), nullable=True)
    CVSS = sql.Column(sql.String(1000), nullable=True)
    AffectedProducts = sql.Column(sql.JSON, nullable=True)
    ExploitAvailability = sql.Column(sql.String(1000), nullable=True)
    Patch = sql.Column(sql.String(1000), nullable=True)
    Description = sql.Column(sql.String(1000), nullable=True)
    AttackVector = sql.Column(sql.String(1000), nullable=True)
    Impact = sql.Column(sql.String(1000), nullable=True)
    References = sql.Column(sql.JSON, nullable=True)
    LastUpdated = sql.Column(sql.DateTime, nullable=True)


class DarkTrace(BaseFeed):

    def save_to_db(self):
        total = 0
        logger.debug("Done with saving...")
        return total
