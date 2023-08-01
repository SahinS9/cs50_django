from django.shortcuts import render

from django.http import HttpResponse, Http404


def index(request):
    return render(request,'singlepage2/index.html')


texts = [
    'Text 1 for the first Page',
    'Text 2 shows page 2 is here',
    'Text 3 identifies 3 page with example'
]


def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num-1])
    else:
        raise Http404('No Section')


