from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobdetail', views.jobdetail, name='jobdetail'),
    path("jobdetail/<str:id>",views.jobdetail,name ="jobdetail"),
]