from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Piplinedata
from django.urls import reverse
from django.utils import timezone
# Create your views here.

def index(request):
    try:
        entry = Piplinedata.objects.get(pk=1)
    except:
        post = Piplinedata()
        post.pk = 1
        post.vibrationCount = 0
        post.latitude = 9.0542
        post.longitude = 7.4851
        post.date_created = timezone.now()
        post.save()

    return render(request, 'index.html',{'saveVcount':entry})

def counting(request):
    va1 = float(request.GET['inputCount'])
    post = Piplinedata.objects.get(pk = 1)
    post.vibrationCount = va1
    post.save()
    return HttpResponseRedirect(reverse ('index'))

def GPS(request):
    va1 = float(request.GET['gpslatitude'])
    va2 = float(request.GET['gpslongitude'])
    post = Piplinedata.objects.get(pk = 1)
    post.latitude = va1
    post.longitude = va2
    post.save()
    return HttpResponseRedirect(reverse ('index'))