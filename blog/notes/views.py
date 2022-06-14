from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

@login_required(login_url="/members/login/")
def index(request):
	latest_blog = Blog.objects.order_by('-pub_date')
	context = {
		"latest_blog": latest_blog,
	}
	return render(request, "notes/index.html", context)

@login_required(login_url="/members/login/")
def details(request, blog_id):
	try:
		blog = Blog.objects.get(pk=blog_id)
		return render(request, "notes/blog.html", {"blog": blog})
	except Blog.DoesNotExist:
		raise Http404("Server Fucked Up")
