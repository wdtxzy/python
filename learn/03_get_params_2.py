import urllib.request
import urllib.parse
import urllib.response
import string

def get_params():
    url = "http://www.baidu.com/s?wd="

    params = {
        "wd":"中文",
        "key":"张",
        "value":"san"
    }
    str_params = urllib.parse.urlencode(params)
    result = url + str_params
    print(result)

    #将带有中文的url转译成计算可以识别的url
    end_url = urllib.parse.quote(result,safe=string.printable)
    response = urllib.request.urlopen(end_url)
    data = response.read().decode("utf-8")
    print(data)

get_params()