from django.urls import path
from . import views


app_name = 'articles'


urlpatterns = [
    path('post/', views.article_post, name='post'),
    path('detail/<int:pk>/', views.articles_detail, name='detail'),
    path('category/<str:category>/', views.article_category, name='category')
]