import os
from django.http import HttpResponse
from django.shortcuts import render
from facebooktools.tools import uploadVideo

from tiktoktools.models import Tiktofb
from tiktoktools.tools import downloadVideo, getAllNewVideoLinks

# Create your views here.
def index(request):
    return HttpResponse("tiktok tools index page")


def uploadVideoFromTiktok(request):
    # Get all the Tiktofb records
    tiktofbs = Tiktofb.objects.all()

    for tiktofb in tiktofbs:
        # Check if Tiktok has a new video
        downloadLinks,VideoIds=getAllNewVideoLinks(tiktofb.tiktok_id, tiktofb.tiktok_last_video_id)
        downloadLinks.reverse()
        VideoIds.reverse()
        for i in range(len(downloadLinks)):
            if tiktofb.tiktok_last_video_id=="None":
                videoPath=downloadVideo(downloadLinks[-1],VideoIds[-1])
                if(videoPath==None):
                    continue
                # Upload the last video to Facebook
                postId=uploadVideo(tiktofb.fb_page_id, videoPath, message="")
                # Update the Tiktofb record with the last video ID
                tiktofb.tiktok_last_video_id = VideoIds[-1]
                tiktofb.save()
                os.remove(videoPath)
                break
            videoPath=downloadVideo(downloadLinks[i],VideoIds[i])
            if(videoPath==None):
                continue
            postId=uploadVideo(tiktofb.fb_page_id, videoPath, message="")
            tiktofb.tiktok_last_video_id = VideoIds[i]
            tiktofb.save()
            os.remove(videoPath)


    return HttpResponse("Videos uploaded successfully")
    