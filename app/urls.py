from django.urls import path
from . import views
from products.views import products, productDetail
from blog.views import news, post, create_post
from contacts import contact

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', products, name='products'),
    path('products/<int:produto_id>/', productDetail, name='productDetail'),
    path('news/', news, name='news'),
    path('news/<int:noticia_id>/', post, name='post'),
    path('news/create/', create_post, name='createPost'),
    path('contact/', contact, name='contact'),

]
