# Create your views here.
from django.http import HttpResponse
from django.conf import settings
from models import *
def index(request):
    return HttpResponse('hello world')

def insert(request):
    b = Blog(name = "liwei's blog", tagline = "tagline")
    b.save()
    b = Blog(name = "seckcoder's blog", tagline = "tagline")
    b.save()
    author = Author(name = "liwei", email = "liwei@jike.com")
    author.save()
    author = Author(name = "seckcoder", email = "seckcoder@gmail.com")
    author.save()
    return HttpResponse('insert finished')
