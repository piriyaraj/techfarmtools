from django.shortcuts import render
from django.http import HttpResponse
from cineulagam.models import Post
# Create your views here.
from . import tools
def index(request):
    return HttpResponse("index page")

def extract(request):
    tools.extractPost()
    return HttpResponse("index page")

def getLastPost(request):
    link=Post.objects.filter(extract=False).order_by("-created")[0]
    return HttpResponse(link.link)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def setExtracted(request):
    print("hello")
    try:
        link=request.POST['link']
        print(link)
        postLinkObj=Post.objects.get(link=link)
        postLinkObj.extract=True
        postLinkObj.save()  
        return HttpResponse("done")
    except:
        return HttpResponse("error")