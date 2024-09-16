from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('posts/list', views.PostListView.as_view(), name='post-list'),
    path('post/detail/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('search', views.SearchView.as_view(), name='search'),
    path('posts/category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('posts/tag/<int:pk>', views.TagDetailView.as_view(), name='tag-detail')
]
