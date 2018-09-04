from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.index, name='index'),
    path('display', views.display, name='display_db'),
    path('add', views.add, name='add_entry'),
    path('update/<int:id>', views.update, name='update'),
    path('boot', TemplateView.as_view(template_name = 'boot.html'), name='boot'),
]