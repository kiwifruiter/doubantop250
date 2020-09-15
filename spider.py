import urllib.request, urllib.error
import re
import bs4


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    # datalist = getData(baseurl)
    # savepath = ".\\豆瓣电影Top250.xls"
    # 3.保存数据
    # saveData(savepath)
    # askURL("https://movie.douban.com/top250?start=0")


# if __name__ == "__main__":
#     main()
# 影片详情的规则
findLink = re.compile(r'<a href="(.*?)">')
# 找到影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # 让换行符包含在字符中
# 影片的片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 找到评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findinq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
findBd = re.compile(r'<p class="">(.*)</p>', re.S)


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 1):
        url = baseurl + str(i * 25)
        html = askURL(url)
        # 2.逐一解析数据
        soup = bs4.BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_='item'):
            # print(item) 查看电影item全部信息
            data = []
            item = str(item)
            # 影片的超链接
            link = re.findall(findLink, item)[0]
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle, item)
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                etitle = titles[1].replace("/", "")
                data.append(etitle)

            else:
                data.append(titles[0])
                data.append('')  # 外国名留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.compile(findJudge, item)[0]
            data.append(judgeNum)

            inq = re.compile(findinq, item)[0]
            if len(inq) != 0:
                inq = inq[0].replace(".", "")
                data.append(inq)
            else:
                data.append("")

            bd = re.findall(findBd.item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', "", bd)
            bd = re.sub('/', "", bd)
            data.append(bd.strip())

            datalist.append(data)

    print(datalist)
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

    return html


# 保存数据
def saveData(savepath):
    print("save....")


if __name__ == "__main__":
    main()
