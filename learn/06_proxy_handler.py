import urllib.request

def create_proxy_handler():
    url = "http://www.baidu.com"

    #添加代理
    proxy = {
        #免费的写法
        "http":"http://120.77.249.46:8080"
    }
    #代理处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)
    #创建opener
    proxy_opener = urllib.request.build_opener(proxy_handler)

    #拿着代理ip发送请求
    responese = proxy_opener.open(url)
    print(responese)

create_proxy_handler()