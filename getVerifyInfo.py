#accountTypeSpider
#autor:Jade
#创建日期:2020/9/8
#-*- coding:utf-8 -*-



#<i class="icon-vip icon-vip-g">金V
#<i class="icon-vip icon-vip-y">黄V
#<i class="icon-vip icon-vip-b">蓝


import urllib.request
from urllib import parse
from bs4 import BeautifulSoup
import re

def get_V_info(user_name):
    find_type = re.compile(r'<i class="icon-vip icon-vip-(.)"></i>')
    url = 'https://s.weibo.com/user?q={}&Refer=weibo_user'.format(parse.quote(user_name))

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode("utf-8")
    bs = BeautifulSoup(html, 'html.parser')
    search_result = bs.find_all("div", class_="info")
    if (len(search_result) > 0):
        account_info = search_result[0]
        account_type = re.findall(find_type, str(account_info))
        if (len(account_type) > 0):
            v_info = account_type[0]
            print(user_name,str(v_info))
            return str(v_info)
        else:
            print(user_name,"无")
            return "无类型"
    else:
        print(user_name,"无用户")
        return "无用户"







