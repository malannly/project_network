from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import random
from datetime import datetime
from .admin import PostAdmin, GroupAdmin
from .models import Group, Post
# Create your views here.
def index(request):
    context = {
    'title': 'main page',
    'content': get_ten_last_posts(),
    'text': 'Good day\n Nice time\n Great deal\n',
    'time': datetime.now(),
    }
    return render(request, 'posts/index.html', context)
def groups(request):
    context = {
    'title': 'group list',
    'groups': get_groups()
    }
    return render(request, 'posts/group_list.html', context)
    #return HttpResponse('Groups page')
def group(request, slug):
    group = get_object_or_404(Group, slug = slug)
    posts = Post.objects.filter(group = group).order_by('-pub_date')[:10]
    context = {
    'group': group,
    'posts': posts,
    }
    return render(request, 'posts/group.html', context)
'''def fizzbazz():
    return ['fizzbazz' if i%15==0 else 'fizz' if i%3==0 else 'bazz' if i%5==0 else i
        for i in range(1,11)]'''
def get_groups():
    return Group.objects.all()
def get_ten_last_posts():
    return Post.objects.order_by('-pub_date')[0:10]