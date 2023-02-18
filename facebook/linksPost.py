
import datetime
from itertools import dropwhile, takewhile
import shutil
import time
import os
import instaloader
import requests
from facebook.models import Actress,Metadata
import pytz

    
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
    return res.content