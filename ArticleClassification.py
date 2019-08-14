try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

from bs4 import BeautifulSoup

def getAllDoxyDonkeyPosts(url,links):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response)
    for a in soup.findAll('a'):
        try:
            url = a['href']
            title = a['title']
            if title == "Older Posts":
                print(title, url)
                links.append(url)
                getAllDoxyDonkeyPosts(url,links)
        except:
            title = ""
    return

blogUrl = "http://doxydonkey.blogspot.in"
links = []
getAllDoxyDonkeyPosts(blogUrl,links)

def getDoxyDonkeyText(testUrl):
    request = urllib2.Request(testUrl)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response)
    mydivs = soup.findAll("div", {"class":'post-body'})
    
    posts =[]
    for div in mydivs:
        posts+=map(lambda p:p.text.replace("?"," "), div.findAll("li"))
    return posts

doxyDonkeyPosts = []
for link in links:
    doxyDonkeyPosts+=getDoxyDonkeyText(link)