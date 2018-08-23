import  urllib.request

if __name__ == '__main__':
    url = 'http://news.ifeng.com/a/20180823/59949209_0.shtml?_zbs_baidu_news'

    rsp = urllib.request.urlopen(url)
    print(type(rsp))
    print(rsp)

    print("URL:{0}".format(rsp.geturl()))
    print("Info:{0}".format(rsp.info()))
    print("Code:{0}".format(rsp.getcode()))

    html = rsp.read()

    html = html.decode()
