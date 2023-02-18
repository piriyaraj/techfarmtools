import requests
from bs4 import BeautifulSoup
def extractPost(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    if len(soup.find_all('iframe', class_='note-video-clip')) > 0:
        return 0,0,0,0
    title=soup.title.text
    cont=soup.find("div",{"class":"ds-content"})
    for a in cont.find_all('a'):
        a.replace_with(a.contents[0])

    imgTags=cont.find_all("img")
    imgUrls=[]
    for i in imgTags:
        imgUrls.append(i.attrs['src'])
    text=cont
     # Extract the site description
    meta_desc = soup.find("meta", {"name": "description"})
    if meta_desc:
        site_desc = meta_desc["content"]
    else:
        site_desc = title
    return title,text,imgUrls,site_desc
    pass

res=extractPost("https://cineulagam.com/article/vaathi-movie-review-1676677963")
print(res)