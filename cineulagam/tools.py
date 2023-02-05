import requests
from bs4 import BeautifulSoup
import re
from cineulagam.models import Post
from django.db import IntegrityError
import time

url = "https://sitemap.cineulagam.com/articles-0.xml"

def getAllUrlsFromSitemap(sitemapLink:str)->list:
    reqs = requests.get(sitemapLink)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    wa_links=re.findall(r'<loc>(.+?)</loc>',soup.prettify().replace("\n","").replace(" ",""))
    return wa_links

def extractPost():
    postLinks=getAllUrlsFromSitemap(url)
    lastlink=Post.objects.filter().order_by("-created")[0].link
    ind=postLinks.index(lastlink)
    postLinks=postLinks[:ind]
    postLinks.reverse()
    for post in postLinks:
        try:
            Post.objects.create(link=post)
        except IntegrityError:
            pass
        pass


if __name__=="__main__":
    print(getAllUrlsFromSitemap(url))
