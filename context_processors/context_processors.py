from blog.models import Post, Category, Tag



def recent_posts(request):
    recent_posts = Post.objects.all().order_by('-created_at')[:3]

    return {'recent_posts': recent_posts}


def categories(request):
    categories = Category.objects.all()

    return {'categories': categories}


def tags(request):
    tags = Tag.objects.all()

    return {'tags': tags}



