from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('all_posts/', views.AllPostsList.as_view(), name='all_posts'),
    path('all_bloggers/', views.AllBloggersList.as_view(), name='all_bloggers'),
    path('blogger/<int:pk>/', views.BloggerDetailView.as_view(), name='blogger_detail'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
]