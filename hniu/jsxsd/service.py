import json
import requests
from hniu import config
from hniu.jsxsd import utils
import logging

logger = logging.getLogger(__name__)

asc = config.AcademicSystem()


class Service():
    def __init__(self):
        self.session = requests.Session()

    def login(self, username, password):
        encoded = self.authEncoded()
        code = utils.encoded(username, password, encoded)
        logger.debug("account {}, encoded {}".format(username, code))
        url = asc.getApi(asc.登陆)
        payload = {
            "userAccount": username,
            "userPassword": password,
            "encoded": code
        }
        req = self.session.post(url=url, data=payload)
        if req.status_code != 200:
            raise requests.RequestException
        return self.session.cookies.get_dict()

    def authEncoded(self):
        url = asc.getApi(asc.验证码)
        req = self.session.post(url=url)
        self.session.cookies.update(req.cookies)
        encoded = req.text
        return encoded
