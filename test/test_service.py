from cmath import log
from re import S
import re
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
    def test_getZc(self):
        logger.info(utils.getSelfKbContent(cookies={
            "JSESSIONID": 'CFCBC9DF87E77D9E234AB63828E86A45',
            "bzb_jsxsd": '800642C1965891C00EDFA6F3295AFAC2'
        },data={
            "xnxq01id": '2021-2022-2'
        }))
    def test_kbcontent_match(self):
        text = "Web企业级开发技术%毛杰辉其他1-10,12(周)[01-02节]【25-南院教学楼】25-406M通知单编号：202120222303(讲课:24,实验:92)"
        r = re.match(r'(?P<kb>.*)%(?P<teacher>.*)其他(?P<week>.*)\[(?P<time>.*)]【(?P<floor>.*)】(?P<room>.*)通知单编号：(?P<code>.*)\((?P<keshi>.*)\)',text)
        print(r.groups())
    def test_kbcontent_tiyu(self):
        text = "大学体育2%陈亮军其他%1-6,8-16(周)[07-08节]通知单编号：2020202120029360(讲课:1,实验:29)"
        r = re.match(r'(?P<kb>.*)%(?P<teacher>.*)(其他|讲师（高校）|助教（高校）|讲师（中专）|副教授|实验师|高等学校教师)%(?P<week>.*)\[(?P<time>.*)]通知单编号：(?P<code>.*)\((?P<keshi>.*)\)',text)
        print(r.groups())

if __name__ == "__main__":
    unittest.main()