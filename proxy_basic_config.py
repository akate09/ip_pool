#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by shimeng on 17-9-19

"""

代理网址及解析字典

status 代理状态, 若不想爬取此网站,可以将status设置为非active的任意值
request_method , 请求方法, 必写, 当为post的时候, 必须定义提交的post_data, 否则会报错.因项目的特殊性, 提交的数据中会带有页码数据, 所以在这里将
post_data 定义为列表, 里面的数据为字典格式
url 代理网址

parse_type  解析类型,默认提供: xpath, re

(1) xpath
ip_port_together ip地址和ip的端口是否在一个字段中
若为地址与端口在一起,则建议key为ip_address_and_port
若为地址与端口不在一起,则建议key为ip_address, ip_port

(2) re
若解析的类型为re, 则ip_port_together可以为任意的值
parse_method中只有一个键: _pattern

parse_func 解析函数, 默认值为system, 当需要使用自定义的解析函数的时候, 需要显式的定义该字段为自定义的解析函数
解析函数要有四个参数, 分别为value, html_content, parse_type, website_name

header 因网址较多, 所以在这里可以自定义头
"""

from custom_get_ip.get_ip_from_peauland import peauland_parser, peauland_format_post_data, peauland_header

# 定义检测的目标网站
target_urls = ['https://www.baidu.com', 'https://httpbin.org/get']

# 数据库集合名
collection_name = 'proxy'

# 数据库中IP存活时间阀值, 超过及对其重新检测
over_time = 1800

url_parse_dict = {
    # data5u
    'data5u': {
        'status':'active',
        'request_method':'get',
        'url': ['http://www.data5u.com/free/{tag}/index.shtml'.format(tag=tag) for tag in ['gngn', 'gnpt', 'gwgn', 'gwpt']],
        'parse_type': 'xpath',
        'ip_port_together': False,
        'parse_method':{
            'ip_address': '//ul[@class="l2"]/span[1]/li/text()',
            'ip_port': '//ul[@class="l2"]/span[2]/li/text()',
        },
        'parse_func': 'system',
        'header':{
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (    KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
               'Host':'www.data5u.com'},

        'cookies': {'auth':'ded3925b8c5e8d7e76d8c53adddb126a','UM_distinctid':'15ec17818ff255-08c779ac69a09f-3e63430c-100200-15ec1781900338','JSESSIONID':'6E325854F0AEBA3263BC134728466385','Hm_lvt_3406180e5d656c4789c6c08b08bf68c2':'1506484427,1506499967,1506658845','Hm_lpvt_3406180e5d656c4789c6c08b08bf68c2':'1506658845','CNZZDATA1260383977':'1191357251-1506482906-%7C1506659015','auth':'ded3925b8c5e8d7e76d8c53adddb126a'}
    },

    # xicidaili
    'xicidaili': {
        'status': 'active',
        'request_method': 'get',
        'url': ['http://www.xicidaili.com/nn/{page}'.format(page=page) for page in range(1, 10)],
        'parse_type': 'xpath',
        'ip_port_together': False,
        'parse_method': {
            'ip_address': '//table/tr/td[2]/text()',
            'ip_port': '//table/tr/td[3]/text()',
        },
        'parse_func': 'system'

    },

    # 66ip
    '66ip': {
        'status': 'active',
        'request_method': 'get',
        'url': ['http://www.66ip.cn/{page}.html'.format(page=page) for page in range(1, 10)],
        'parse_type': 're',
        'ip_port_together': False,
        'parse_method': {
            '_pattern': '<tr><td>([\d\.]*?)</td><td>(.*?)</td>',
        },
        'parse_func': 'system'
        }
}

'''
    # proxydb
    # 这个也是国外的一个网站,如果你的网络无法访问,可以将status改为inactive
    # 这个网站采用的post方法, 需要将submit_data定义好, 采用自定义解析函数, 自定义的请求头
    # 如果你也遇到变态的网站, 按照这个进行配置即可
    'proxydb': {
        'status': 'active',
        'request_method': 'post',
        'submit_data':peauland_format_post_data(),
        'url': ['https://proxy.peuland.com/proxy/search_proxy.php'],
        'parse_func': peauland_parser,
        'header': peauland_header()
    },
'''
