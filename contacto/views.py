from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm

def contacto(request):
    post = Post.objects.all()
    return render(request, 'contacto/contacto.html', {'post': post})

def post_detail(request, post_id):
    post=Post.objects.get(id=post_id)

    comments=post.comments.filter(active=True)

    if request.method == 'POST':
        form=CommentForm(request.POST)

        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.post= post 
            new_form.save()
    else:
        form=CommentForm

    return render(request, 'contacto/contacto/post_detail.html', {'post':post, 'comments': comments, 'form': form})
