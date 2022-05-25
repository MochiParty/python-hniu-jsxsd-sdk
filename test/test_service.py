from cmath import log
from re import S
import unittest
from hniu.jsxsd import service
from hniu.jsxsd import utils

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class TestService(unittest.TestCase):
    service = service.Service()
    def test_login(self):
        logger.info(self.service.login('202015310535','Hniu202618@'))
    def test_utils_encoded(self):
        logger.info(utils.encoded('202015310535','asdasd@@@','FV6bSOR8r87Ntv4q0017kACg65f16y03OsjU03J2l2#13313231321312132232'))



if __name__ == "__main__":
    unittest.main()