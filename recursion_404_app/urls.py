

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('fixed', views.fixed,name='fixed'),
    path('security', views.security,name='security'),
    path('signup', views.signup,name='signup'),

    
    
]
