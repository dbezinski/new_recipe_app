from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

    # /recipe_app/recipe/add/
    url(r'recipe/add/$', views.RecipeCreate.as_view(), name='recipe-add'),

    url(r'^$', views.get_index, name='index'),

    ]