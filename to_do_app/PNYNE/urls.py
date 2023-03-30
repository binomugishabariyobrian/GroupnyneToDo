from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('homepage', views.homepage, name='home-page'),
    path('task', views.task, name='task'),
]
