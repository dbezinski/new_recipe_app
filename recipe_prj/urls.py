from django.conf.urls import url, include
from django.contrib import admin
from accounts import views as accounts_views
from accounts.views import register, profile, login, logout
from products import views as product_views
from django.conf import settings
from django.conf.urls.static import static

from recipe_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^recipe_app/', include('recipe_app.urls')),

    #Auth URLs
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    # Blog URLs
    url(r'^reusable_blog/', include('reusable_blog.urls')),

    #Products URLs:
    url(r'^products/$', product_views.all_products, name='products'),
    url(r'payment-accepted/$', views.payment_accepted, name='payment-accepted'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)