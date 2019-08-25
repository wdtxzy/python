import urllib.request
import urllib.response
import random

def load_baidu():
    url = "https://www.baidu.com"

    user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
                       "Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12",
                       "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
                       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"]

    #每次请求的浏览器都不一样
    random_user_agent = random.choice(user_agent_list)

    #创建请求头
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
               }

    # 创建请求对象
    request1 = urllib.request.Request(url, headers=headers)

    #动态添加
    request2 = urllib.request.Request(url)
    request2.add_header("User-Agent", random_user_agent)

    #请求网络数据
    response = urllib.request.urlopen(request2)
    data = response.read().decode("utf-8")
    #打印请求头
    request_headers = request1.get_header("User-agent")
    print(request_headers)

load_baidu()