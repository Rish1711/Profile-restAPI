from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewsets, basename='hello-viewset')
router.register('UserProfile', views.UserProfileViewSet)
router.register('login', views.LoginAPI, basename='login')
router.register('UserProfileFeed', views.UserProfileFeedViewSet)


urlpatterns = [
    url(r'^hello-view/', views.Hello_APIView.as_view()),
    url(r'', include(router.urls)),
]
