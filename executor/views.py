import os
import time
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from executor.models import Tiktoyt
from tiktoktools.tools import downloadVideo, getAllNewVideoLinks
from youtubetools.tools import get_authenticated_service, videoUpload

# Create your views here.
def index(request):
    return HttpResponse("executor tools index page")

# upload video from tiktik to youtube
def tikToYt(request):
    # Get all the Tiktoyt records
    tiktoyts = Tiktoyt.objects.all().order_by('-modified')

    for tiktoyt in tiktoyts:
        # Check if Tiktok has a new video
        downloadLinks,VideoIds=getAllNewVideoLinks(tiktoyt.tiktok_id, tiktoyt.tiktok_last_video_id)
        downloadLinks.reverse()
        VideoIds.reverse()
        print(len(VideoIds))
        authPath=tiktoyt.yt_auth.url
        authPath=settings.MEDIA_ROOT.replace("\\","/") +"/"+ authPath[len(settings.MEDIA_URL):] # get the full path of the yt_auth file
        print(type(authPath),authPath)
        title=tiktoyt.yt_title
        description=tiktoyt.yt_description
        status=tiktoyt.yt_status
        tags=tiktoyt.yt_tags.split(", ")[:2]
        print(tags)
        for i in range(len(downloadLinks)):

            if tiktoyt.tiktok_last_video_id=="None":
                print("new post from the tiktok account")
                videoPath=downloadVideo(downloadLinks[-1],VideoIds[-1])
                if(videoPath==None):
                    continue
                # time.sleep(60)

                postUrl=videoUpload(title,description,videoPath,status,tags,authPath)
                if(postUrl==None):
                    break
                print("postUrl: ",postUrl)
                # Update the Tiktoyt record with the last video ID
                tiktoyt.tiktok_last_video_id = VideoIds[-1]
                tiktoyt.save()
                os.remove(videoPath)
                break
            videoPath=downloadVideo(downloadLinks[i],VideoIds[i])
            print("video path of downloaded video:",str(videoPath))
            if(videoPath==None):
                continue
            # time.sleep(60)
            postUrl=videoUpload(title,description,videoPath,status,tags,authPath)
            if(postUrl==None):
                break
            print("postUrl: ",postUrl)
            tiktoyt.tiktok_last_video_id = VideoIds[i]
            tiktoyt.save()
            os.remove(videoPath)
        return HttpResponse(f'Video uploaded from {tiktoyt.tiktok_id} to {tiktoyt.yt_name}')
    return HttpResponse("No new videos found")
    
    