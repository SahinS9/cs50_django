from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'singlepage1/index.html')


texts = [
    'NOT Text 1 for the first Page',
    'NOT Text 2 shows page 2 is here',
    'NOT Text 3 identifies 3 page with example'
]


def section(request, num):
    if 1<= num <= 3:
        return HttpResponse(texts[num-1])
    else:
        raise Http404('No Such Section')
