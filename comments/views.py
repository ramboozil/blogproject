from django.shortcuts import get_object_or_404, render, redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm
# Create your views here.


def get_post_comments(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()  # 相当于comment.objects.filter(post=post)
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)  # 调用model里面的get_absolute_url方法
