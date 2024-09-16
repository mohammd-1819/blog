from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from .models import Post, Category, Tag, Comment


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 2
    context_object_name = 'posts'


class PostDetailView(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/post_detail.html', {'post': post})

    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        body = request.POST.get('message')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(text=body, post=post, user=request.user, parent_id=parent_id)

        return render(request, 'blog/post_detail.html', {'post': post})


class SearchView(View):
    def get(self, request):
        q = request.GET.get('q')
        posts = Post.objects.filter(title__icontains=q)
        paginator = Paginator(posts, 1)
        page_number = request.GET.get('page')
        objects_list = paginator.get_page(page_number)
        return render(request, 'blog/search_result.html', {'posts': objects_list})


class CategoryDetailView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        posts = category.posts.all()
        paginator = Paginator(posts, 2)
        page_number = request.GET.get('page')
        objects_list = paginator.get_page(page_number)

        return render(request, 'blog/category_post_detail.html', {'posts': objects_list})


class TagDetailView(View):
    def get(self, request, pk):
        tag = get_object_or_404(Tag, id=pk)
        posts = tag.posts.all()
        paginator = Paginator(posts, 2)
        page_number = request.GET.get('page')
        objects_list = paginator.get_page(page_number)
        return render(request, 'blog/tag_detail_posts.html', {'posts': objects_list})
