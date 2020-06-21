from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.



def all_blogs(request):
    blog_apps = Blog.objects.order_by('-date')
    return render(request,'blog_app/all_blogs.html',{'blogs':blog_apps})

def detail(request,blog_app_id):
    blog = get_object_or_404(Blog, pk=blog_app_id)
    return render(request,'blog_app/detail.html' , {'blog':blog})
