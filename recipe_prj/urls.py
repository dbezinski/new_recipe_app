from django.conf.urls import url, include
from django.contrib import admin
from accounts import views as accounts_views
from accounts.views import register, profile, login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^recipe_app/', include('recipe_app.urls')),

    #Auth URLs
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    ]
