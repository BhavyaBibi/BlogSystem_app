from django.shortcuts import render
from django.http import Http404
from .models import Post,Author,subscribe
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def index(request):
    if request.method == 'GET':
	    email = request.GET.get('email')
	    if email:
		    subscribe(email=email).save()

    week_ago = datetime.date.today() - datetime.timedelta(days = 7)
    trends = Post.objects.filter(time_upload__gte = week_ago).order_by('-read')
    TopAuthors =Author.objects.order_by('-rate')[:4]
    AuthorsPost = [Post.objects.filter(auther = author).first() for author in TopAuthors]
  
    parms = {
		'posts': Post.objects.all(),
		'trends': trends[:5],
		'author_post':AuthorsPost,
		'pop_post': Post.objects.order_by('-read')[:9],
	}
    return render(request, 'index.html', parms)
	
def about(request):
	parms = {
		'title': 'About | Blogproject',

		}
	return render(request, 'about.html', parms)

def post(request):
    return render(request, 'blog-single.html')

def contact(request):
	
	return render(request, 'contact.html')

def search(request):
	

	return render(request, 'all.html')

def view_all(request, query):
	

	return render(request, 'all.html')