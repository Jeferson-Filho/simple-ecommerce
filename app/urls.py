from django.urls import include, path
from . import views
from products.views import products, productDetail, productCreate
from blog.views import news, post, create_post
from contacts.views import contact
from user.views import address, profile, register
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', products, name='products'),
    path('products/<int:product_id>/', productDetail, name='productDetail'),
    path('news/', news, name='news'),
    path('news/<int:post_id>/', post, name='post'),
    path('news/create/', create_post, name='createPost'),
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', profile, name='profile'),
    path('address/', address, name='address'),
    path('cadastrar-produto/', productCreate, name='productCreate'),
    path('cart/', include('cart.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
