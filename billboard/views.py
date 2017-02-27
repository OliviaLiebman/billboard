from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required()
def post_list(request):
    # post_text = request.POST.get('the_post')

    title = request.POST.get('title')
    content = request.POST.get('content')
    author = request.POST.get('author')
    created_date = timezone.now()

    x = Post(title=title, text = content, author=author, created_date=created_date)
    x.save()
    return HttpResponseRedirect('/')


def index(request):
    # instance = Post.objects.all()
    # instance.delete()

    return render(request, 'billboard.html', {'posts': Post.objects.all()})

