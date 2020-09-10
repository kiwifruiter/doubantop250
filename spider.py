import urllib.request,urllib.error
import re
import bs4


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xls"
    # 3.保存数据
    # saveData(savepath)
    askURL("https://movie.douban.com/top250?start=0")


# if __name__ == "__main__":
#     main()

# 爬取网页
def getData(baseurl):
    datalist = []
    # 2.逐一解析数据
    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 85.0.4183.83Safari / 537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        assert isinstance(request, object)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        assert isinstance(html, object)
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print((e.reason))

    # return html


# 保存数据
def saveData(savepath):
    print("save....")


if __name__ == "__main__":
    main()
