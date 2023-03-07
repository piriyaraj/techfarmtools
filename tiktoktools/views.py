import os
import time
from django.http import HttpResponse
from django.shortcuts import render
from facebooktools.tools import shareOnGroup, uploadVideo

from tiktoktools.models import Tiktofb
from tiktoktools.tools import downloadVideo, getAllNewVideoLinks

# Create your views here.
def index(request):
    return HttpResponse("tiktok tools index page")

# upload video from tiktik to facebook
def uploadVideoFromTiktok(request):
    # Get all the Tiktofb records
    tiktofbs = Tiktofb.objects.all().order_by('-modified')

    for tiktofb in tiktofbs:
        # Check if Tiktok has a new video
        downloadLinks,VideoIds=getAllNewVideoLinks(tiktofb.tiktok_id, tiktofb.tiktok_last_video_id)
        downloadLinks.reverse()
        VideoIds.reverse()
        print(len(VideoIds))
            
        for i in range(len(downloadLinks)):
            if tiktofb.tiktok_last_video_id=="None":
                videoPath=downloadVideo(downloadLinks[-1],VideoIds[-1])
                if(videoPath==None):
                    continue
                time.sleep(60)

                # Upload the last video to Facebook
                postId=uploadVideo(tiktofb.fb_page_id, videoPath, message="")
                shareOnGroup(tiktofb.fb_page_id,postId)
                print("postId: ",postId)
                # Update the Tiktofb record with the last video ID
                tiktofb.tiktok_last_video_id = VideoIds[-1]
                tiktofb.save()
                os.remove(videoPath)
                break
            videoPath=downloadVideo(downloadLinks[i],VideoIds[i])
            if(videoPath==None):
                continue
            time.sleep(60)
            postId=uploadVideo(tiktofb.fb_page_id, videoPath, message="")
            shareOnGroup(tiktofb.fb_page_id,postId)
            
            print("postId: ",postId)
            tiktofb.tiktok_last_video_id = VideoIds[i]
            tiktofb.save()
            os.remove(videoPath)
        return HttpResponse(f'Video uploaded from {tiktofb.tiktok_id} to {tiktofb.fb_page_name}')
    return HttpResponse("No new videos found")
    
    