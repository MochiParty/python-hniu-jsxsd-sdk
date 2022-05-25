from json.tool import main
import unittest
import requests
from hniu.jsxsd import service


class TestMethod(unittest.TestCase):
    def test(self):
        print("hello world~")
    def test_cookie(self):
        req = requests.get(url="http://hniu.js.ayou10031.cn")
        print(req.cookies)
    def test_getClass(self):
        s = requests.Session()
        cookies = {
            "bzb_jsxsd": "4FC5D1E03EBACA3ACC418ECDD7FF394B",
            "JESSIONID": "395D90FD3FBAB4299418D24A28E56C6D"
        }
        s.cookies.update(cookies)
        result = s.get("http://hniu.js.ayou10031.cn/jsxsd/xskb/xskb_list.do")
        print(result.status_code)
        # print(result.text)
        main = s.get("http://hniu.js.ayou10031.cn/jsxsd/xskb/xskb_list.do")
        print(main.text)
        # jar = requests.utils.cookiejar_from_dict(cookies)
        # req =requests.get(url="http://hniu.js.ayou10031.cn/jsxsd/xskb/xskb_list.do",cookies=jar)
        # print(req.text)
        # main = requests.get(url="http://hniu.js.ayou10031.cn/jsxsd/xskb/xskb_list.do")
        # print(main.text)

if __name__ == "main":
    unittest.main()