class AcademicSystem:
    URL = "http://hniu.js.ayou10031.cn"
    主页 = "/jsxsd/framework/xsMain.htmlx",
    主页课表 = "/jsxsdframework/main_index_loadkb.htmlx?rq={0}&sjmsValue={1}&xnxqid={2}",
    学期理论课表 = "/jsxsd/xskb/xskb_list.do"
    登陆 = "/Logon.do?method=logon"
    验证码 = "/Logon.do?method=logon&flag=sess"
    职位 = "(其他|讲师（高校）|助教（高校）|讲师（中专）|副教授|实验师|高等学校教师)"

    def getApi(self, key) -> str:
        return AcademicSystem.URL + key