from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import job
from .serializers import jobSerializer,indexSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def index(request):
    data = job.objects.all()
    s = indexSerializer(data,many=True)
    return render(request, 'index.html',{'data':s.data[::-1]})

@csrf_exempt
def jobdetail(request,id=None):
    data = job.objects.filter(jobid=id)
    s = jobSerializer(data,many=True)
    return render(request, 'jobdetail.html',{'data':s.data})
