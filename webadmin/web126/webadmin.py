# # coding=utf8
from selenium import webdriver
from cfg import *
import time
import os


class webadmin(object):
    # 设置工作路径
    # os.chdir('C:\Users\Administrator\Desktop\pwd')#绝对路径

    # 判断登录的网址、用户和密码
    def webwzusps(self):
        web = '0'
        while web != '126' and web != '163':
            web = raw_input('请输入登录的网站（126/163）：')
            if web == '':
                print ('请输入网站！')
            elif web == '126':
                url = url126
                user = userpasswd126[userpasswd126.rfind(':') + 1:userpasswd126.rfind('/')]
                passwd = userpasswd126[userpasswd126.rfind('/') + 1:]
                print user, passwd
                return {"name":user,"mima":passwd,"wangzi":url}
            elif web == '163':
                url = url163
                user = userpasswd163[userpasswd163.rfind(':') + 1:userpasswd163.rfind('/')]
                passwd = userpasswd163[userpasswd163.rfind('/') + 1:]  # return url, user, passwd
                print user, passwd
                return {"name":user,"mima":passwd,"wangzi":url}
            elif web == 'quit':
                break
            else:
                print '请输入正确的网站！'

    # 打开浏览器，设置登录的网页，自动登录
    def runweb(self, us, pw, url):
        # url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=48021271_11_hao_pg&wd=126&rsv_spt=1&oq=126&rsv_pq=b83f03df0002c0d2&rsv_t=99db7Nk%2FtdbFbQcewdm3fEYyzjb5rz90qo%2FC99h2f18YT3pOGoUA3JUNB6jwYa7aDtjdRhcM0GaX&rqlang=cn&rsv_enter=0"
        web = webdriver.Chrome()
        web.get(url)
        web.find_element_by_id("op_email3_username").send_keys(us)
        web.find_element_by_class_name("op_email3_password").send_keys(pw)
        web.find_element_by_class_name("c-btn").click()
    #获取邮件内容
    def xzfj(self):
        web.find_element_by_css_selector("/")

# 调用函数
wo = webadmin()
yh = wo.webwzusps()
print '用户名：', yh['name'], '\n密码：', yh['mima'], '\n网址：', yh['wangzi']
wo.runweb(us=yh['name'], pw=yh['mima'], url=yh['wangzi'])
