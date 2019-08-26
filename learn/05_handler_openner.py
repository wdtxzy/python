import urllib.request

def handler_openner():

    #系统的urlopen并没有添加代理的功能所以需要我们自定义这个功能
    #安全 套接层 ssl第三方的CA数字证书
    #http80端口个 和 https 443端口

    url = "http://www.baidu.com"

    #创建自己的处理器
    handler = urllib.request.HTTPHandler
    #创建自己的opener
    opener = urllib.request.build_opener(handler)
    #用自己创建的opener访问数据
    response = opener.open(url)
    data = response.read()
    print(data)

handler_openner()