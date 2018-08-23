from urllib import request

if __name__ == '__main__':
    url = "https://jobs.zhaopin.com/CC566985081J00171958205.htm"
    rsp = request.urlopen(url)

    html = rsp.read()
    print(type(html))

    html = html.decode("utf-8")

    print(html)