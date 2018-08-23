''''
利用parse模块模拟post请求
分析百度词典
分析步骤：
1.打开F12
2.尝试输入单词girl，发现每敲一个字母后面都有请求
3.请求地址是 http://fanyi.baidu.com/sug
4.利用NetWork-ALL-Hearders，查看，发现FormData的值是kw：girl
5.检查返回内容格式，发现返回的是json格式内容==>需要用到json包
'''

from urllib import  request,parse
import  json

'''
大致流程是：
1.利用data构造内容，然后urlopen打开
2.返回一个json格式的结果
3.结果就应该是girl是释义
'''

baseurl = 'http://fanyi.baidu.com/sug'

data={
    'kw':'girl'
}

data = parse.urlencode(data).encode("utf-8")

headers = {
    'Content-Length':len(data)
}

rsp = request.urlopen(baseurl,data=data)

json_data = rsp.read().decode()

print(json_data)

json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data['data']:
    print(item['k'],"--",item['v'])