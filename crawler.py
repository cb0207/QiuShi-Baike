import re
import urllib.request
import urllib.error

def crawl(url,page):
    req=urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/52.0.2743.116Safari/537.36Edge/15.15063")
    req.timeout=5
    try:
        content=str(urllib.request.urlopen(req).read().decode('utf-8'))
    except urllib.error.URLErrorasease:
        if hasattr(e,"code"):
            print(page+"页，"+e.code)

    match1='divclass="content".+?</div>'
    content1=re.findall(match1,content,re.S)
    contentList=[]
    for i in content1:
        contentList.extend(re.findall('<span>.+?</span>',i,re.S))

    fhandle=open('Z:\\Downloads\\practise\\urllib\\qiushi.txt','a',encoding='utf-8')
    for i in contentList:
        fhandle.write(i.replace('<span>','**')+'\n\n')
        fhandle.close()


def lastPage(url):
	req=urllib.request.Request(url)
	req.add_header("User-Agent","Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/52.0.2743.116Safari/537.36Edge/15.15063")
	html=str(urllib.request.urlopen(req).read())
	match_lastPage='<spanclass="page-numbers">.+?</span>'
	page=re.findall(match_lastPage,html)
	i=len(page)
	lastPage=re.findall('\d+',page[i-1])
	return lastPage[0]


pageNum=lastPage('https://www.qiushibaike.com/1hr/page/1')

for page in range(1,int(pageNum)):
	url="https://www.qiushibaike.com/1hr/page/"+str(page)
	crawl(url,page)
print("done")
