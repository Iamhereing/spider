import  urllib.request
import chardet

if __name__ == '__main__':
    url = 'http://news.ifeng.com/a/20180823/59949209_0.shtml?_zbs_baidu_news'

    rsp = urllib.request.urlopen(url)

    html = rsp.read()

    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    html = html.decode(cs.get("encoding","utf-8"))
    print(html)