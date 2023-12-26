

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('report_pothole', views.report_pothole, name='report_pothole'),
    path('login',views.User,name="login")
]
