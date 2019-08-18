import urllib.request
import urllib.parse
import string

def get_method_params():

    url = "http://www.baidu.com/s?wd="
    #拼接字符串（汉字）
    name = "美女"
    #python 的解释器不支持汉字，需要转译
    final_url = url + name
    print(final_url)
    encode_new_url = urllib.parse.quote(final_url,safe=string.printable)
    print(encode_new_url)
    #使用代码发送网络请求
    response = urllib.request.urlopen(encode_new_url)
    print(response)
    # 读取内容 bytes类型
    data = response.read()
    print(data)
    # 将文件内容转成字符串
    str_data = data.decode("utf-8")
    print(str_data)

get_method_params()