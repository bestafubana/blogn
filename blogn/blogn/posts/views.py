from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Comment
from django.db.models import Case, Value, When,F
from django.db.models.functions import Coalesce, Concat, Cast

# Create your views here.
def home(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'posts/index.html', {'posts': posts})

def post_single(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    commentsQuery = """SELECT * FROM posts_comment 
        WHERE post_id = %s 
        ORDER BY IFNULL(parent_comment_id, id), CAST(id AS text) || CAST( IFNULL(parent_comment_id, id) AS text)"""

    comments = Comment.objects.raw(commentsQuery, [post.id])
    
    return render(request, 'posts/single.html', {'post': post, 'comments': comments})