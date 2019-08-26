import urllib.request

def proxy_user():

    proxy_list = [
        {"http":"60.182.124.231:61234"},
        {"http":"113.116.246.235:9797"},
        {"http":"114.106.77.223:808"},
        {"http":"119.96.160.50:8888"}
    ]

    for proxy in proxy_list:
        print(proxy)
        #利用遍历出来的ip创建处理器
        proxy_handler = urllib.request.ProxyHandler(proxy)
        #创建opener
        opener = urllib.request.build_opener(proxy_handler)

        try:
            response = opener.open("https://www.baidu.com",timeout=1)

        except Exception as e:
            print(e)

proxy_user()