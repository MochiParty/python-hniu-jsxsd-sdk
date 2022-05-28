import json
import re
import logging
from pyquery import PyQuery as pq
from hniu import config
from requests_html import  HTMLSession,HTML

"""
教务系统登陆加密工具
"""
def encoded(username: str, password: str, decoded: str) -> str:
    arr = decoded.split('#')
    scode = arr[0]
    sxh = arr[1]
    code = username+"%%%"+password
    encoded = ""
    for i in range(len(code)):
        if i < 20:
            encoded = encoded + code[i:i+1] + scode[0:int(sxh[i:i+1])]
            scode = scode[int(sxh[i:i+1]):len(scode)]
        else:
            encoded = encoded + code[i:len(code)]
            break
    return encoded

"""
获取个人课表 需要传入
    cookies:
        JESSIONID
        bzb_jsxsd
    data:
        zc # 周次
        xnxq01id # 学年学期
"""
def getSelfKbContent(cookies=dict(JSESSIONID=None,bzb_jsxsd=None),data=dict(zc='',xnxq01id=None,sfFd=1,wkbkc=1)):
    session = HTMLSession()
    r = session.post(url=config.AcademicSystem.getApi(config.AcademicSystem,config.AcademicSystem.学期理论课表),cookies=cookies,data=data)
    doc = r.html.pq
    teacher = doc('font').items()
    for tt in teacher:
        name = tt.attr('title')
        if name == "教师":
            text = tt.text()
            tt.html('%'+ text+"%")
    doc = """{}""".format(doc)
    r = HTML(html=doc).pq
    kbcontent = r.find('.kbcontent')
    kb = {}
    for content in kbcontent:
        id = content.get('id')
        week = id[-3:-2]
        if not kb.get(week) :
            kb[week] = []
        if id[-1:] == '2':
            # logging.debug("id {} {}".format(id,content.text_content()))
            text = str(content.text_content()).replace('\xa0','').split("---------------------")
            kb[week].append(text)
    # logging.debug(json.dumps(kb,ensure_ascii=False))
    for k,arrays in kb.items():
        # logging.debug("{} {}".format(k,values))
        for values in arrays:
            for v in range(values.__len__()):
                    """
                    教师名
                    职位
                    课程
                    周次
                    节次
                    教学楼栋
                    教室
                    编号
                    课时
                    """
                    cdata = {
                        'teacher': '',
                        'prefix': '',
                        'course': '',
                        'week':'',
                        'time': '',
                        'floor': '',
                        'room': '',
                        'code': '',
                        'keshi': ''
                    }
                    if len(values[v]) <= 0:
                        values.__setitem__(v,None)
                        continue
                    text = values[v]
                    try:
                        r = re.match(r'(?P<course>.*)%(?P<teacher>.*)'+config.AcademicSystem.职位+'%(?P<week>.*)\[(?P<time>.*)]【(?P<floor>.*)】(?P<room>.*)通知单编号：(?P<code>\w*)(?P<keshi>.*)',text)
                        if not r.groups(): raise AttributeError
                        cdata['course'] = r.group(0)
                        cdata['teacher'] = r.group(2)
                        cdata['course'] = r.group(1)
                        cdata['prefix'] = r.group(3)
                        cdata['week'] = r.group(4)
                        cdata['time'] = r.group(5)
                        cdata['floor'] = r.group(6)
                        cdata['room'] = r.group(7)
                        cdata['code'] = r.group(8)
                        cdata['keshi'] = r.group(9)
                    except AttributeError:
                        r = re.match(r'(?P<course>.*)%(?P<teacher>.*)'+config.AcademicSystem.职位+'%(?P<week>.*)\[(?P<time>.*)]通知单编号：(?P<code>.*)\((?P<keshi>.*)\)',text)
                        cdata['course'] = r.group(0)
                        cdata['teacher'] = r.group(2)
                        cdata['course'] = r.group(1)
                        cdata['prefix'] = r.group(3)
                        cdata['week'] = r.group(4)
                        cdata['time'] = r.group(5)
                        cdata['code'] = r.group(6)
                        cdata['keshi'] = r.group(7)
                    values.__setitem__(v,cdata)
                    # logging.debug(json.dumps(values,ensure_ascii=False))
    logging.debug(json.dumps(kb,ensure_ascii=False))
    return json.dumps(kb,ensure_ascii=False)