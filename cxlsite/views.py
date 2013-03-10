from django.http import Http404,HttpResponse
import datetime

def hello(request):
    return HttpResponse("hello chen xiao long ")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>it is now %s.</body></html>" % now
    return HttpResponse(html)
def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html="<html><body>in %s hours,it will be %s.</body></html>"%(offset,dt)
    return HttpResponse(html)