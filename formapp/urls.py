from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_post_list, name='blog_post_list'),
    path('post/add/', views.blog_post_add_edit, name='blog_post_add'),
    path('post/edit/<int:pk>/', views.blog_post_add_edit, name='blog_post_edit'),
    path('post/<int:pk>/', views.blog_post_detail, name='blog_post_detail'), 
]
