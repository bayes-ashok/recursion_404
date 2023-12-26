

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('report_pothole', views.report_pothole, name='report_pothole'),
    path('other_reports', views.other_reports, name='other_reports'),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('events', views.events,name='events'),
    path('all_events/', views.all_events, name='all_events'), 
]
