from .import views
from django.urls import path


urlpatterns = [

    path('',views.index,name='weather'),
    path('<int:pk>',views.delete_city,name='delete'),


]