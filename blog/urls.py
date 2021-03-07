from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('category/<str:slug>/', views.PostsByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', views.PostsByTag.as_view(), name='tag'),
    path('post/<str:slug>/', views.GetPost.as_view(), name='post'),
    path('search/', views.Search.as_view(), name='search'),
]