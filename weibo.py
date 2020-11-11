# coding=utf-8
import random

import bs4
import requests
import time


def getUrl(url):
    head = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/85.0.4183.102 Safari/537.36) ",
        'cookie': "SINAGLOBAL=9086145751118.078.1535803385598; "
                  "SCF=AuvB67tgEG6J3XSRnru9VqM89v9OYFNbnrEh2FUgs1Xj6n3L8Q6XcqUkZWA0G5EzNI_XmtqCiaC7forIPdgZz-Y.; "
                  "login_sid_t=d989ce13b9d19bb41960868ace7030d5; cross_origin_proto=SSL; "
                  "Ugrow-G0=589da022062e21d675f389ce54f2eae7; TC-V5-G0=4de7df00d4dc12eb0897c97413797808; "
                  "wb_view_log=1536*8641.25; _s_tentry=www.baidu.com; Apache=58468024151.55894.1600825351921; "
                  "ULV=1600825351926:28:5:3:58468024151.55894.1600825351921:1600783745752; SUHB=0pHh-KdxkeM5FN; "
                  "wb_view_log_6542741913=1536*8641.25; secsys_id=35dc24cafd62542481369fd030f4d926; "
                  "YF-V5-G0=f5a079faba115a1547149ae0d48383dc; "
                  "webim_unReadCount=%7B%22time%22%3A1600830557423%2C%22dm_pub_total%22%3A0%2C%22chat_group_client"
                  "%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D; "
                  "SUB=_2AkMoNjNVdcPxrAVUnPoSyGrrbY5H-jyb41qjAn7uJhMyAxh77gc0qSVutBF-XCtjwmlpItHIuLTf0yPeDPgupCeA; "
                  "SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WWYdcdFXiDnjiEweYuyAuFq; UOR=jx3.xoyo.com,"
                  "widget.weibo.com,login.sina.com.cn; "
                  "YF-Page-G0=f1e19cba80f4eeaeea445d7b50e14ebb|1600830829|1600830552; "
                  "TC-Page-G0=1ae767ccb34a580ffdaaa3a58eb208b8|1600837816|1600837816 "
    }
    req = requests.get(url, headers=head)
    return req.json()["data"]["html"]


baseUrl = "https://weibo.com/aj/v6/comment/big?ajwvr=6&id=4552051469848548&from=singleWeiBo&__rnd=1600845688663"
# 用于生成下一个url
root_comment_max_id = ""  # 上一页最后一条评论减一
sum_comment_number = 0  # 已展示的comment
for i in range(1, 200):
    data = getUrl(baseUrl + "&page=" + str(i) + "&sum_comment_number=" + str(i * 15) + "&root_comment_max_id=" + str(
        root_comment_max_id))
    soup = bs4.BeautifulSoup(data, "lxml")
    comment = soup.findAll('div', class_='list_li S_line1 clearfix')
    root_comment_max_id = int(comment[-1]["comment_id"]) - 1
    for j in comment:
        print(j.find("div", class_='WB_text').text[1:])
    print(i)
