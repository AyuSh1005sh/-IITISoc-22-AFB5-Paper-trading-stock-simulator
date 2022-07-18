
from django.contrib import admin
from django.urls import path , include ,re_path

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
  
    path('social/', include('social.apps.django_app.urls', namespace='social')),
    path('auth/', include('rest_framework_social_oauth2.urls')),
]

