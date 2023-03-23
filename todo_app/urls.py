from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name='todo.home'),
path('add', views.add, name='todo.add'),
path('modify/<int:id>', views.modify, name='todo.modify'),
path('delete/<int:id>', views.delete, name='todo.delete'),
path('update/<int:id>', views.update, name='todo.update')
]