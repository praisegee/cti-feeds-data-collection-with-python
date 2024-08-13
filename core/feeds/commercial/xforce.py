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
# ABUSE_CH_URL = "https://urlhaus-api.abuse.ch/v1/urls/recent/limit/3/"
Session = sessionmaker(engine)


class XForceModel(BaseModel):
    __tablename__ = "x_force"

    """
    {
      "url": "latencychecker-botnet-20240812172029.xyz",
      "created": "2024-08-12T17:23:00.000Z"
    }
    """
    url = sql.Column(sql.String(1000), nullable=True)
    created = sql.Column(sql.DateTime, nullable=True)
    date_added = sql.Column(sql.DateTime, default=sql.func.now(), nullable=True)


class XForce(BaseFeed):

    def __init__(self, api_key=None):
        BaseFeed.__init__(self, api_key)
        self.api_url = X_FORCE__URL

    def save_to_db(self):
        total = 0
        api_key = config("X_FORCE_API_KEY")
        api_password = config("X_FORCE_API_PASSWORD")
        api_token = config("X_FORCE_API_TOKEN")
        headers = {"Authorization": f"Bearer {api_token}"}
        # response = self._request(headers=headers)
        response = requests.get(
            X_FORCE__URL, auth=HTTPBasicAuth(api_key, api_password)
        )  # headers=headers)

        try:
            total = len(response["rows"])
        except:
            pass

        if response is not None:
            with Session() as session:
                for data in response["rows"]:
                    logger.info(f"Added {data['url']} to DB.")
                    session.add(XForceModel(**data))
                session.commit()
        else:
            logger.error("No data found.")

        logger.debug("Done with saving...")
        return total
