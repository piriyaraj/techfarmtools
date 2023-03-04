
import datetime
from itertools import dropwhile, takewhile
import json
import shutil
import time
import os
import instaloader
import requests
from facebooktools.models import Actress, Facebook_group,Metadata
import pytz
import facebook as fb

    
def postAlink(groupName,postLink,content):
    try:
        data=Metadata.objects.get(name=groupName)
        access_token = data.key
        pageId=data.pageId
    except Exception as e:
        print(e)
        access_token= None
        return "check the access token in admin pannel"
    args = dict()
    args["message"] = content
    args["link"] = postLink
    url = f"https://graph.facebook.com/{pageId}/feed?access_token=" + access_token
    res=requests.post(url, data=args)
    json_data = res.json()
    id_value = json_data['id']
    return id_value

def shareOnGroup(pageId, postId):
    try:
        data=Metadata.objects.get(pageId=pageId)
        access_token = data.key
        pageId=data.pageId
    except Exception as e:
        print(e)
        access_token= None
        return "check the access token in admin pannel"

    groupIds=Facebook_group.objects.filter(page__pageId=pageId)
    asafb = fb.GraphAPI(access_token)

    for group in groupIds:
        try:
            res=asafb.put_object(group.groupId, "feed",link=f'www.facebook.com/{pageId}/posts/{postId}')
            return res.json()
            pass
        except:
            pass
        
def test():
    result=postAlink("actress_gallery","https://nammacinema.walinking.link/%E0%AE%88%E0%AE%B0%E0%AE%AE%E0%AE%BE%E0%AE%A9-%E0%AE%B0%E0%AF%8B%E0%AE%9C%E0%AE%BE%E0%AE%B5%E0%AF%87-2-%E0%AE%9A%E0%AF%80%E0%AE%B0%E0%AE%BF%E0%AE%AF%E0%AE%B2%E0%AF%8D-%E0%AE%A8%E0%AE%9F%E0%AE%BF/","")
    print("page post: ",result)
    result=shareOnGroup(*result.split("_"))
    print("group post: ",result)
    