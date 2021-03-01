from django.urls import path
from .  import views

urlpatterns= [
    path('', views.viewlist, name="viewlist"),

]
