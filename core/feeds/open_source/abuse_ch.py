import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker

from core.database import BaseModel, engine
from core.feeds.base import BaseFeed
from utils.logger import Logger

logger = Logger(__name__).get_logger()
ABUSE_CH_URL = "https://urlhaus-api.abuse.ch/v1/urls/recent/"
# ABUSE_CH_URL = "https://urlhaus-api.abuse.ch/v1/urls/recent/limit/3/"
Session = sessionmaker(engine)


class AbuseModel(BaseModel):
    __tablename__ = "abuse_ch"

    """
    {
        "id": 3097950,
        "urlhaus_reference": "https://urlhaus.abuse.ch/url/3097950/",
        "url": "http://117.248.175.222:57673/bin.sh",
        "url_status": "online",
        "host": "117.248.175.222",
        "date_added": "2024-08-09 16:22:06 UTC",
        "threat": "malware_download",
        "blacklists": {
            "spamhaus_dbl": "not listed",
            "surbl": "not listed"
        },
        "reporter": "geenensp",
        "larted": "true",
        "tags": [
            "32-bit",
            "elf",
            "mips",
            "Mozi"
        ]
    }
    """

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


class AbuseCH(BaseFeed):

    def __init__(self, api_key=None):
        BaseFeed.__init__(self, api_key)
        self.api_url = ABUSE_CH_URL

    def save_to_db(self):
        response = self._request()
        # data = response["urls"][0]

        if response is not None:
            with Session() as session:
                for data in response["urls"]:
                    logger.info(f"Added {data['id']}: {data['url']} to DB.")
                    session.add(AbuseModel(**data))
                # session.add(AbuseModel(**data))
                session.commit()
        else:
            logger.error("No data found.")

        logger.debug("Done with saving...")
