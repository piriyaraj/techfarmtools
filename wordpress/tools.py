import os
import time
import requests
from bs4 import BeautifulSoup
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
import re
from facebooktools.tools import postAlink, shareOnGroup
from wordpress.models import Nammacinema_post
from django.db import IntegrityError

file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)
def unicodeChange(text):
    text = text.replace("ஸ்ரீ", "=")
    text = text.replace(",", ">")
    text = text.replace("ஜௌ", "n[s")
    text = text.replace("ஜோ", "N[h")
    text = text.replace("ஜொ", "n[h")
    text = text.replace("ஜா", "[h")
    text = text.replace("ஜி", "[p")
    text = text.replace("ஜீ", "[P")
    text = text.replace("ஜு", "[{")
    text = text.replace("ஜூ", "[_")
    text = text.replace("ஜெ", "n[")
    text = text.replace("ஜே", "N[")
    text = text.replace("ஜை", "i[")
    text = text.replace("ஜ்", "[;")
    text = text.replace("ஜ", "[")
    text = text.replace("கௌ", "nfs")
    text = text.replace("கோ", "Nfh")
    text = text.replace("கொ", "nfh")
    text = text.replace("கா", "fh")
    text = text.replace("கி", "fp")
    text = text.replace("கீ", "fP")
    text = text.replace("கு", "F")
    text = text.replace("கூ", "$")
    text = text.replace("கெ", "nf")
    text = text.replace("கே", "Nf")
    text = text.replace("கை", "if")
    text = text.replace("க்", "f;")
    text = text.replace("க", "f")
    text = text.replace("ஙௌ", "nqs")
    text = text.replace("ஙோ", "Nqh")
    text = text.replace("ஙொ", "nqh")
    text = text.replace("ஙா", "qh")
    text = text.replace("ஙி", "qp")
    text = text.replace("ஙீ", "qP")
    text = text.replace("ஙு", "*")
    text = text.replace("ஙூ", "*")
    text = text.replace("ஙெ", "nq")
    text = text.replace("ஙே", "Nq")
    text = text.replace("ஙை", "iq")
    text = text.replace("ங்", "q;")
    text = text.replace("ங", "q")
    text = text.replace("சௌ", "nrs")
    text = text.replace("சோ", "Nrh")
    text = text.replace("சொ", "nrh")
    text = text.replace("சா", "rh")
    text = text.replace("சி", "rp")
    text = text.replace("சீ", "rP")
    text = text.replace("சு", "R")
    text = text.replace("சூ", "R+")
    text = text.replace("செ", "nr")
    text = text.replace("சே", "Nr")
    text = text.replace("சை", "ir")
    text = text.replace("ச்", "r;")
    text = text.replace("ச", "r")
    text = text.replace("ஞௌ", "nQs")
    text = text.replace("ஞோ", "NQh")
    text = text.replace("ஞொ", "nQh")
    text = text.replace("ஞா", "Qh")
    text = text.replace("ஞி", "Qp")
    text = text.replace("ஞீ", "QP")
    text = text.replace("ஞு", "*")
    text = text.replace("ஞூ", "*")
    text = text.replace("ஞெ", "nQ")
    text = text.replace("ஞே", "NQ")
    text = text.replace("ஞை", "iQ")
    text = text.replace("ஞ்", "Q;")
    text = text.replace("ஞ", "Q")
    text = text.replace("டௌ", "nls")
    text = text.replace("டோ", "Nlh")
    text = text.replace("டொ", "nlh")
    text = text.replace("டா", "lh")
    text = text.replace("டி", "b")
    text = text.replace("டீ", "B")
    text = text.replace("டு", "L")
    text = text.replace("டூ", "^")
    text = text.replace("டெ", "nl")
    text = text.replace("டே", "Nl")
    text = text.replace("டை", "il")
    text = text.replace("ட்", "l;")
    text = text.replace("ட", "l")
    text = text.replace("ணௌ", "nzs")
    text = text.replace("ணோ", "Nzh")
    text = text.replace("ணொ", "nzh")
    text = text.replace("ணா", "zh")
    text = text.replace("ணி", "zp")
    text = text.replace("ணீ", "zP")
    text = text.replace("ணு", "Z")
    text = text.replace("ணூ", "Z}")
    text = text.replace("ணெ", "nz")
    text = text.replace("ணே", "Nz")
    text = text.replace("ணை", "iz")
    text = text.replace("ண்", "z;")
    text = text.replace("ண", "z")
    text = text.replace("தௌ", "njs")
    text = text.replace("தோ", "Njh")
    text = text.replace("தொ", "njh")
    text = text.replace("தா", "jh")
    text = text.replace("தி", "jp")
    text = text.replace("தீ", "jP")
    text = text.replace("து", "J")
    text = text.replace("தூ", "J}")
    text = text.replace("தெ", "nj")
    text = text.replace("தே", "Nj")
    text = text.replace("தை", "ij")
    text = text.replace("த்", "j;")
    text = text.replace("த", "j")
    text = text.replace("நௌ", "nes")
    text = text.replace("நோ", "Neh")
    text = text.replace("நொ", "neh")
    text = text.replace("நா", "eh")
    text = text.replace("நி", "ep")
    text = text.replace("நீ", "eP")
    text = text.replace("நு", "E")
    text = text.replace("நூ", "E}")
    text = text.replace("நெ", "ne")
    text = text.replace("நே", "Ne")
    text = text.replace("நை", "ie")
    text = text.replace("ந்", "e;")
    text = text.replace("ந", "e")
    text = text.replace("னௌ", "nds")
    text = text.replace("னோ", "Ndh")
    text = text.replace("னொ", "ndh")
    text = text.replace("னா", "dh")
    text = text.replace("னி", "dp")
    text = text.replace("னீ", "dP")
    text = text.replace("னு", "D")
    text = text.replace("னூ", "D}")
    text = text.replace("னெ", "nd")
    text = text.replace("னே", "Nd")
    text = text.replace("னை", "id")
    text = text.replace("ன்", "d;")
    text = text.replace("ன", "d")
    text = text.replace("பௌ", "ngs")
    text = text.replace("போ", "Ngh")
    text = text.replace("பொ", "ngh")
    text = text.replace("பா", "gh")
    text = text.replace("பி", "gp")
    text = text.replace("பீ", "gP")
    text = text.replace("பு", "G")
    text = text.replace("பூ", "G+")
    text = text.replace("பெ", "ng")
    text = text.replace("பே", "Ng")
    text = text.replace("பை", "ig")
    text = text.replace("ப்", "g;")
    text = text.replace("ப", "g")
    text = text.replace("மௌ", "nks")
    text = text.replace("மோ", "Nkh")
    text = text.replace("மொ", "nkh")
    text = text.replace("மா", "kh")
    text = text.replace("மி", "kp")
    text = text.replace("மீ", "kP")
    text = text.replace("மு", "K")
    text = text.replace("மூ", "%")
    text = text.replace("மெ", "nk")
    text = text.replace("மே", "Nk")
    text = text.replace("மை", "ik")
    text = text.replace("ம்", "k;")
    text = text.replace("ம", "k")
    text = text.replace("யௌ", "nas")
    text = text.replace("யோ", "Nah")
    text = text.replace("யொ", "nah")
    text = text.replace("யா", "ah")
    text = text.replace("யி", "ap")
    text = text.replace("யீ", "aP")
    text = text.replace("யு", "A")
    text = text.replace("யூ", "A+")
    text = text.replace("யெ", "na")
    text = text.replace("யே", "Na")
    text = text.replace("யை", "ia")
    text = text.replace("ய்", "a;")
    text = text.replace("ய", "a")
    text = text.replace("ரௌ", "nus")
    text = text.replace("ரோ", "Nuh")
    text = text.replace("ரொ", "nuh")
    text = text.replace("ரா", "uh")
    text = text.replace("ரி", "up")
    text = text.replace("ரீ", "uP")
    text = text.replace("ரு", "U")
    text = text.replace("ரூ", "&")
    text = text.replace("ரெ", "nu")
    text = text.replace("ரே", "Nu")
    text = text.replace("ரை", "iu")
    text = text.replace("ர்", "u;")
    text = text.replace("ர", "u")
    text = text.replace("லௌ", "nys")
    text = text.replace("லோ", "Nyh")
    text = text.replace("லொ", "nyh")
    text = text.replace("லா", "yh")
    text = text.replace("லி", "yp")
    text = text.replace("லீ", "yP")
    text = text.replace("லு", "Y")
    text = text.replace("லூ", "Y}")
    text = text.replace("லெ", "ny")
    text = text.replace("லே", "Ny")
    text = text.replace("லை", "iy")
    text = text.replace("ல்", "y;")
    text = text.replace("ல", "y")
    text = text.replace("ளௌ", "nss")
    text = text.replace("ளோ", "Nsh")
    text = text.replace("ளொ", "nsh")
    text = text.replace("ளா", "sh")
    text = text.replace("ளி", "sp")
    text = text.replace("ளீ", "sP")
    text = text.replace("ளு", "S")
    text = text.replace("ளூ", "Sh")
    text = text.replace("ளெ", "ns")
    text = text.replace("ளே", "Ns")
    text = text.replace("ளை", "is")
    text = text.replace("ள்", "s;")
    text = text.replace("ள", "s")
    text = text.replace("வௌ", "nts")
    text = text.replace("வோ", "Nth")
    text = text.replace("வொ", "nth")
    text = text.replace("வா", "th")
    text = text.replace("வி", "tp")
    text = text.replace("வீ", "tP")
    text = text.replace("வு", "T")
    text = text.replace("வூ", "T+")
    text = text.replace("வெ", "nt")
    text = text.replace("வே", "Nt")
    text = text.replace("வை", "it")
    text = text.replace("வ்", "t;")
    text = text.replace("வ", "t")
    text = text.replace("ழௌ", "nos")
    text = text.replace("ழோ", "Noh")
    text = text.replace("ழொ", "noh")
    text = text.replace("ழா", "oh")
    text = text.replace("ழி", "op")
    text = text.replace("ழீ", "oP")
    text = text.replace("ழு", "O")
    text = text.replace("ழூ", "*")
    text = text.replace("ழெ", "no")
    text = text.replace("ழே", "No")
    text = text.replace("ழை", "io")
    text = text.replace("ழ்", "o;")
    text = text.replace("ழ", "o")
    text = text.replace("றௌ", "nws")
    text = text.replace("றோ", "Nwh")
    text = text.replace("றொ", "nwh")
    text = text.replace("றா", "wh")
    text = text.replace("றி", "wp")
    text = text.replace("றீ", "wP")
    text = text.replace("று", "W")
    text = text.replace("றூ", "W}")
    text = text.replace("றெ", "nw")
    text = text.replace("றே", "Nw")
    text = text.replace("றை", "iw")
    text = text.replace("ற்", "w;")
    text = text.replace("ற", "w")
    text = text.replace("ஹௌ", "n`s")
    text = text.replace("ஹோ", "N`h")
    text = text.replace("ஹொ", "n`h")
    text = text.replace("ஹா", "`h")
    text = text.replace("ஹி", "`p")
    text = text.replace("ஹீ", "`P")
    text = text.replace("ஹு", "{`")
    text = text.replace("ஹூ", "`_")
    text = text.replace("ஹெ", "n`")
    text = text.replace("ஹே", "N`")
    text = text.replace("ஹை", "i`")
    text = text.replace("ஹ்", "`;")
    text = text.replace("ஹ", "`")
    text = text.replace("ஷௌ", "n\\s")
    text = text.replace("ஷோ", "N\\h")
    text = text.replace("ஷொ", "n\\h")
    text = text.replace("ஷா", "\\h")
    text = text.replace("ஷி", "\\p")
    text = text.replace("ஷீ", "\\P")
    text = text.replace("ஷு", "\\{")
    text = text.replace("ஷூ", "\\_")
    text = text.replace("ஷெ", "n\\")
    text = text.replace("ஷே", "N\\")
    text = text.replace("ஷை", "i\\")
    text = text.replace("ஷ்", "\\;")
    text = text.replace('ஷ', '\\')
    text = text.replace("ஸௌ", "n]s")
    text = text.replace("ஸோ", "N]h")
    text = text.replace("ஸொ", "n]h")
    text = text.replace("ஸா", "]h")
    text = text.replace("ஸி", "]p")
    text = text.replace("ஸீ", "]P")
    text = text.replace("ஸு", "]{")
    text = text.replace("ஸூ", "]_")
    text = text.replace("ஸெ", "n]")
    text = text.replace("ஸே", "N]")
    text = text.replace("ஸை", "i]")
    text = text.replace("ஸ்", "];")
    text = text.replace("ஸ", "]")
    text = text.replace("அ", "m")
    text = text.replace("ஆ", "M")
    text = text.replace("இ", ",")
    text = text.replace("ஈ", "<")
    text = text.replace("உ", "c")
    text = text.replace("ஊ", "C")
    text = text.replace("எ", "v")
    text = text.replace("ஏ", "V")
    text = text.replace("ஐ", "I")
    text = text.replace("ஒ", "x")
    text = text.replace("ஓ", "X")
    text = text.replace("ஔ", "xs")
    text = text.replace("ஃ", "/")
    return text



def setposted(link):
    try:
        postLinkObj=Nammacinema_post.objects.get(link=link)
        postLinkObj.extract=True
        postLinkObj.save()  
        return True
    except:
        return False

def downloadImages(imgUrlList)->None:
    imgPath="wordpress/images/"
    if(not os.path.exists(os.path.abspath(imgPath))):
        os.makedirs(os.path.abspath(imgPath))
    for i in os.listdir(os.path.abspath(imgPath)):
        os.remove(os.path.abspath(imgPath+i))

    for i in range(len(imgUrlList)):
        reqs = requests.get(imgUrlList[i])
        try:
            soup = BeautifulSoup(reqs.text, 'html.parser')
            picclass=soup.findAll("div",id="pictures-list")[0]
            imgtag=picclass.findAll("img")[0]
            img_url=imgtag.get_attribute_list("src")[0]
            res=requests.get(img_url)
        except:
            res=reqs
        img_title=os.path.abspath(imgPath+str(i)+".jpg")
        file = open(img_title,'wb')
        for chunk in res.iter_content(10000):
            file.write(chunk)
        file.close()

# input:posturl
# output: title,text,photos links
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

def addLogo():
    preImages=os.listdir(os.path.abspath("wordpress/images/"))
    for i,m in enumerate(preImages):
        makePostImge(i)
def makePostImge(no)->None:
    imgPath="wordpress/imagesTemp/"
    if(not os.path.exists(os.path.abspath(imgPath))):
        os.makedirs(os.path.abspath(imgPath))
    preImages=os.listdir(os.path.abspath("wordpress/images/"))

    cinePhoto=Image.open(os.path.abspath("wordpress/images/"+preImages[no%len(preImages)]))
    logo=Image.open(os.path.abspath("wordpress/mediaImage/cine_time_logo.png"))
    
    new_width = int(cinePhoto.size[0]/5)
    wpercent = (new_width/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((new_width,hsize))
    cinePhotox,cinePhotoy=cinePhoto.size
    logoPhotox,logoPhotoy=logo.size
    cinePhoto.paste(logo,(cinePhotox-logoPhotox,cinePhotoy-logoPhotoy))
    cinePhoto = cinePhoto.convert('RGB')
    cinePhoto.save("wordpress/imagesTemp/"+str(no)+".jpg")

def uploadImage():
    imgUrls=[]
    imgIds=[]
    preImages=os.listdir(os.path.abspath("wordpress/imagesTemp/"))
    for i in preImages:
        url = "https://nammacinema.walinking.link/wp-json/nammacinema/v1/uploadImage"
        file = {'file': open(os.path.abspath("wordpress/imagesTemp/"+i),'rb')}

        response = requests.post(url, files=file)
        
        imgUrls.append("/wp-content"+response.json()["imgUrl"].replace("\\","").split("/wp-content")[1])
        imgIds.append(response.json()["imgId"])
    return imgUrls,imgIds
    
def clear():
    clearList=["wordpress/images","wordpress/imagesTemp"]
    for i in clearList:
        tempImages=os.listdir(os.path.abspath(i))
        for j in tempImages:
            os.remove(os.path.abspath(i+"/"+j))
def uploadPost(title,description,imgId=0):
    url = "https://nammacinema.walinking.link/wp-json/nammacinema/v1/createpost"
    data = {
        'title': title,
        'imgId':imgId,
        'description':description
        # any other data you need to send to the API function
    }
    files = {'html_file': open(os.path.abspath("wordpress/output.html"), 'rb')}   

    response = requests.post(url, data=data, files=files)
    return response
def run():
    clear()
    extractPostUrls()
    try:
        postUrl=Nammacinema_post.objects.filter(extract=False).order_by("-created")[0].link
    except:
        return "no new posts"
    # try:
    title,text,imgUrls,description=extractPost(postUrl)
    if(title==0):
        res=setposted(postUrl)
        # print("Video post:",title)
        return "Video post "+title
    # print(title)
    downloadImages(imgUrls)
    time.sleep(60)
    addLogo()
    
    imgUrls,imgIds=uploadImage()

    content=formatContent(text,imgUrls)
    with open(os.path.abspath("wordpress/output.html"), 'w', encoding='utf-8') as f:
        f.write(str(content))
    if imgIds:
        res=uploadPost(title,description,imgIds[0]).json()
    else:
        res=uploadPost(title,description).json()

    res1=setposted(postUrl)
    try:
        result=uploadLinkOnFacebook(res["postlink"],title)
    except Exception as e:
        return str(e)
    # print("Facebook post: ",result)
    return "post uploaded"
    # print(res["postLink"])

        
    # except Exception as e:
    #     print(e)
    # clear()

def uploadLinkOnFacebook(url,message):
    tokenName="actress_gallery"
    result1 = postAlink(tokenName,url,message)
    print("page post: ",result1)
    result=shareOnGroup(*result1.split("_"))
    return result1
def formatContent(cont,imgUrls):
    imgTag=cont.find_all("img")
    for i in imgTag:
        i["src"]=imgUrls[imgTag.index(i)]
    return cont

def test():
    run()
    # res=uploadLinkOnFacebook("https://nammacinema.walinking.link/%e0%ae%aa%e0%ae%bf%e0%ae%b0%e0%ae%aa%e0%ae%b2-%e0%ae%a8%e0%ae%9f%e0%ae%bf%e0%ae%95%e0%ae%b0%e0%af%8d-%e0%ae%9a%e0%ae%bf%e0%ae%a4%e0%af%8d%e0%ae%a4%e0%ae%be%e0%ae%b0%e0%af%8d%e0%ae%a4%e0%af%8d%e0%ae%a4/","பிரபல நடிகர் சித்தார்த்தின் லேட்டஸ்ட் புகைப்படங்கள்")
    # print(res)
    # run()
    return
    postUrl=Nammacinema_post.objects.filter(extract=False).order_by("-created")[0].link
    postUrl="https://cineulagam.com/article/actor-ajith-kumar-net-worth-house-car-collections-1676458124"
    title,cont,imgUrls=extractPost(postUrl)
    # downloadImages(imgUrls)
    content=formatContent(cont,imgUrls)
    return "hello"

url = "https://sitemap.cineulagam.com/articles-0.xml"

def getAllUrlsFromSitemap(sitemapLink:str)->list:
    reqs = requests.get(sitemapLink)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    wa_links=re.findall(r'<loc>(.+?)</loc>',soup.prettify().replace("\n","").replace(" ",""))
    return wa_links

def extractPostUrls():
    postLinks=getAllUrlsFromSitemap(url)
    try:
        lastlink=Nammacinema_post.objects.filter().order_by("-created")[0].link
        ind=postLinks.index(lastlink)
        
    except:
        lastlink=""
        ind=100

    postLinks=postLinks[:ind]
    postLinks.reverse()
    for post in postLinks:
        try:
            Nammacinema_post.objects.create(link=post)
        except IntegrityError:
            pass
        pass


if __name__=="__main__":
    print(getAllUrlsFromSitemap(url))
