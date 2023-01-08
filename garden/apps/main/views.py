from django.shortcuts import render
from django.conf import settings

def media_admin(requset):
    return {'media_url':settings.MEDIA_URL,}

# Create your views here.
def index(request):
    return render(request,'main/index.html')