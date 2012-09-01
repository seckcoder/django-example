# Create your views here.
from django.http import HttpResponse, Http404
from django.conf import settings
from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response
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

def posts(request):
    posts = Blogpost.objects.all()
    return render_to_response("posts.html", {'posts':posts},
                              RequestContext(request))

def test_js(request):
    return render_to_response('test_js.html', {}, RequestContext(request))
def author_detail(request, name):
    return render_to_response('author_detail.html', {'name':name}, RequestContext(request))

def post(request, title):
    try:
        post = Post.objects.get(title=title)
    except:
        return Http404()
    data = {
        'post':post
    }
    template = loader.get_template('post.html')
    context = Context(data)
    output = template.render(context)
    return HttpResponse(output)
