

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('report_pothole', views.report_pothole, name='report_pothole'),
    path('other_reports', views.other_reports, name='other_reports'),
    path('signup-post',views.signup_post,name="signup_post"),
    path('login-check',views.login_check,name="login_check"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('events', views.events,name='events'),
    path('view', views.view,name='poll'),
    path('all_events/', views.all_events, name='all_events'), 
    path('security', views.security,name='security'),
    path('submit-poll', views.submit_poll,name='submitpoll'),

]
