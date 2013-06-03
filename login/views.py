# Create your views here.
import json
import gearman
from gearman import GearmanClient
from django.http import HttpResponse
from models import Author
from django.forms.models import model_to_dict
from django.shortcuts import render_to_response

def login(request):
    return render_to_response('index.html')


def getin(request):
    AllUser=Author.objects.all()

    username=request.POST.get('usern')
    password=request.POST.get('passw')
    Nameresult=Author.objects.get(usern=username)
    if Nameresult!=None:
        UserDict=model_to_dict(Nameresult)
        if UserDict['passw']==password:
             return render_to_response('service.html',{"alluser":AllUser})
        else:
            return render_to_response('index.html')
    else:
         return render_to_response('index.html')


def getdata(request):
    DataList=[]
    for ModelData in Author.objects.all():
        DictData=model_to_dict(ModelData)
        DataList.append(DictData)
    JsonData=json.dumps(DataList)
    PassDataClient=gearman.GearmanClient(['192.168.1.5:4730'])
    completed_job_request=PassDataClient.submit_job("savetask",JsonData)
   # print completed_job_request.result
    return render_to_response('service.html',{"result":completed_job_request.result})
def test(request):
    ttext=request.POST.get('ttext')
    listvalue=request.POST.get('cars')
    PassDataClient=gearman.GearmanClient(['192.168.1.5:4730'])
    JsonData=json.dumps(listvalue)
    completed_job_request=PassDataClient.submit_job("savetask",JsonData)
    return render_to_response('test.html',{"listvalue":listvalue,"ttext":ttext,"result":completed_job_request.result})
    


