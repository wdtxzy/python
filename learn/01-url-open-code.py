import urllib.request

def load_data():
    url = "http://www.baidu.com"
    response = urllib.request.urlopen(url)
    data = response.read()
    print(data)
    #读取内容 bytes类型
    data = response.read()
    print(data)
    #将文件内容转成字符串
    str_data = data.decode("utf-8")
    print(str_data)

load_data()