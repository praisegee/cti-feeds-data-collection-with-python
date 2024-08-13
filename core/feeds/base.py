from abc import abstractmethod, ABC
import requests


class BaseFeed(ABC):
    """An Abstract Base Class for all the feeds"""

    db_table_name = None
    api_url = None
    api_key = None
    headers = {}

    def __init__(self, api_key=None):
        self.api_key = api_key

    @abstractmethod
    def save_to_db(self):
        pass

    def _request(
        self,
        method="GET",
        data: dict | None = None,
        headers: dict | None = None,
        params: dict | None = None,
        auth: dict | None = None,
        **kwargs
    ):
        methods = {"GET": requests.get, "POST": requests.post}
        if headers is not None:
            self.headers.update(headers)
        try:
            req = methods[method.upper()]
        except KeyError:
            raise NotImplementedError("request only accept `GET` and `POST` for now!")
        else:
            resp = req(
                self.api_url,
                data=data,
                headers=headers,
                params=params,
                auth=auth,
                **kwargs
            )
            if resp.status_code == 200:
                return resp.json()
            return None
