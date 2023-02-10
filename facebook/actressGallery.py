import datetime
from itertools import dropwhile, takewhile
import shutil
import time
import os
import instaloader
import requests
from facebook.models import Actress,Metadata
import pytz

try:
    access_token = Metadata.objects.get(name="actress_gallery").key
except Exception as e:
    print(e)
    access_token= None
print(access_token)
facebookId="103874471887645"
# get last download images data

def updateInstaId():
    instaList = [
        'aishwaryarajessh',
        'alya_manasa',
        'anupamaparameswaran96',
        'anushkashettyofficial',
        'athulyaofficial',
        'dharshagupta',
        'gabriellacharlton_',
        'geneliad',
        'hegdepooja',
        'i_nivethathomas',
        'iamaathmika',
        'ihansika',
        'ileana_official',
        'im_raveena_daha',
        'kajalaggarwalofficial',
        'kayal_anandhi',
        'keerthysureshofficial',
        'lakshmimenon967',
        'losliyamariya96',
        'nakshathra.nagesh',
        'namita.official',
        'nikkigalrani',
        'pavithralakshmioffl',
        'poojag.umashankar',
        'raashiikhanna',
        'rakulpreet',
        'rashmika_mandanna',
        'realactress_sneha',
        'sadaa17',
        'saipallaviofficial',
        'samantharuthprabhuoffl',
        'sayyeshaa',
        'shivani_narayanan',
        'shrutzhaasan',
        'simply.asin',
        'simranrishibagga',
        'sivaangi.krish',
        'taapsee',
        'tamannaahspeaks',
        'tamil_rithika',
        'thesunainaa',
        'trishakrishnan',
        'venba.official',
        'yours_anjali',
    ]
    for i in instaList:
        try:
            Actress.objects.create(instaid=i)    
        except:pass
    
# ====================================== upload images ======================================================

# import firebaseSetup


postTime1 = time.time()+10*60
timeDivision = 10*60


def getFullName(userName):
    L = instaloader.Instaloader(
        download_videos=False, save_metadata=False, post_metadata_txt_pattern='')
    t = instaloader.Profile.from_username(L.context, userName)
    return t.full_name
# if __name__=="__main__":
    # run(1)


def postImage(img):
    url = f"https://graph.facebook.com/{facebookId}/photos?access_token=" + access_token

    files = {
        'file': open(img, 'rb'),
    }
    data = {
        "published": False
    }
    r = requests.post(url, files=files, data=data).json()
    return r

# upload multiple image


def multiPostImage(message, imgFolder):
    imgs_id = []
    img_list=os.listdir(imgFolder)

    for img in img_list:
        post_id = postImage(imgFolder+"/"+img)
        print(post_id)
        imgs_id.append(post_id['id'])

    args = dict()
    args["message"] = message
    for img_id in imgs_id:
        key = "attached_media["+str(imgs_id.index(img_id))+"]"
        args[key] = "{'media_fbid': '"+img_id+"'}"
    url = f"https://graph.facebook.com/{facebookId}/feed?access_token=" + access_token
    requests.post(url, data=args)


# =================================================Download image section===============================================
def removeImages(dir):
    img_list=os.listdir(dir)
    for i in img_list:
        os.remove(dir+"/"+i)


def downloadAndUpload():
    count=0
    postObj=Actress.objects.filter().order_by("modified")[0]
    print("insta id: ",postObj.instaid)
    SINCE=postObj.modified

    L = instaloader.Instaloader(
        download_videos=False, save_metadata=False, post_metadata_txt_pattern='')
    try:
        posts = instaloader.Profile.from_username(L.context, postObj.instaid).get_posts()
    except Exception as e:
        return e+"   "+postObj.instaid
    timeList = []
    if SINCE.tzinfo is None:
        SINCE = pytz.utc.localize(SINCE)
    message = ""
    date = ""
    for post in posts:
        print(post.date)
        if post.date.tzinfo is None:
            post_date = pytz.utc.localize(post.date)
        else:
            post_date = post.date
        
        if post_date <= SINCE:
            break
        date = "-"+str(post.date).replace("-",  "_").replace(":", "_").replace(" ", "_")
        # print(date)
        try:
            title = getFullName(postObj.instaid)+">>\n "+post.caption
            message = title
        except:
            title = getFullName(postObj.instaid)
            message = title
        timeList.append(str(post.date))
        L.download_post(post, "actphoto")
        # time.sleep(60)
        count+=1
        
    
    if(os.path.isdir("./actphoto")):
        print(">>>>>>>> in post directory")             
        multiPostImage(message, "./actphoto")
        removeImages("./actphoto")
    postObj.save()
    return f'{postObj.instaid}: {count} photos posted'
              

def test():
    print(os.path.isdir("./facebook∕media∕actphoto-anupamaparameswaran96-2023_02_04_11_33_06"))