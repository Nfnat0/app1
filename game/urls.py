from django.urls import path
from . import views

app_name = 'game'
urlpatterns = [
    path('', views.top, name='top'),
    path('search', views.search, name='search'),
    path('ajax_post_search', views.ajax_post_search, name='ajax_post_search'),
]
