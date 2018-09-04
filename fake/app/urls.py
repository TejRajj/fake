from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.index, name='index'),
    path('forms', views.forms, name='forms'),
    #path('display', views.display, name='display_db'),
    path('boot', TemplateView.as_view(template_name = 'boot.html'), name='boot'),
]