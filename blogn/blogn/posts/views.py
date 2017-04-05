from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'posts/index.html', {'posts': posts})

def post_single(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'posts/single.html', {'post': post})
    
# def post_single(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     return render(request, 'posts/single.html', {'post': post})   