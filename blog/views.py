from django.shortcuts import render
from .models import Post, Category
from django.shortcuts import get_object_or_404
from comments.views import CommentForm
import markdown


# from django.http import HttpResponse


# Create your views here.


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={
        'post_list': post_list,
        # 'welcome': '欢迎来到我的博客首页'
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    return render(request, 'blog/detail.html', context={
        'post': post,
        'form': form,
        'comment_list': comment_list,
    })


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })