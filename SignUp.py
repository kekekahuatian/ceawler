# coding=utf-8
import requests
import bs4
import time
from tkinter import messagebox
import random

baseUrl = "http://10.11.118.156/register/"
host = "http://106.ihuyi.com/webservice/sms.php?"
params = {  # 我
    "mobile": "13251960137",
    "content": "您的验证码是：00000。请不要把验证码泄露给其他人。",
    "account": "C80465601",
    "password": "d5f2a4de9b3e0a8245b4f4967c91e8de",
    "method": "Submit"
}
params0 = {  # 冠希
    "mobile": "18355309597",
    "content": "您的验证码是：00000。请不要把验证码泄露给其他人。",
    "account": "C80465601",
    "password": "d5f2a4de9b3e0a8245b4f4967c91e8de",
    "method": "Submit"
}
params1 = {  # 郑卓
    "mobile": "19157691251",
    "content": "您的验证码是：00000。请不要把验证码泄露给其他人。",
    "account": "C80465601",
    "password": "d5f2a4de9b3e0a8245b4f4967c91e8de",
    "method": "Submit"
}
params2 = {  # 水丽
    "mobile": "19817133840",
    "content": "您的验证码是：00000。请不要把验证码泄露给其他人。",
    "account": "C80465601",
    "password": "d5f2a4de9b3e0a8245b4f4967c91e8de",
    "method": "Submit"
}
params3 = {  # 黄锴健
    "mobile": "18694562825",
    "content": "您的验证码是：00000。请不要把验证码泄露给其他人。",
    "account": "C80465601",
    "password": "d5f2a4de9b3e0a8245b4f4967c91e8de",
    "method": "Submit"
}
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}


def getUrl(url, head):
    try:
        req = requests.get(url, headers=head)
        return req.text
    except BaseException as e:
        print(e)
        getUrl(url, head)


try:
    def star():
        while True:
            html = getUrl(baseUrl, head)
            soup = bs4.BeautifulSoup(html, "html.parser")
            a = soup.text[52:59]
            if a != '报名活动已截止':
                requests.get(host, params=params, headers=head)
                requests.get(host, params=params0, headers=head)
                requests.get(host, params=params1, headers=head)
                requests.get(host, params=params2, headers=head)
                requests.get(host, params=params3, headers=head)
                messagebox.showinfo("报名报名!", "报名报名!报名报名!报名报名!")
                break
            print(time.asctime(time.localtime(time.time())))
            time.sleep(random.randint(5, 10))
except BaseException as e:
    print(e)
    star()
star()
