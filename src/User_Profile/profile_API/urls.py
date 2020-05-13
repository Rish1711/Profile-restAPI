from django.urls import path
from django.conf.urls import include ,url
from . import views

urlpatterns = [
    path('hello_Api/', views.Hello_APIView.as_view() , name='HelloAPI'),

]
