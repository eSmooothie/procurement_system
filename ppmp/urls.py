from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name="logout_user"),
    #ppmp
    path('home/', views.index, name='home'),
    path('home/ppmp', views.index, name='ppmp'),
    path('home/ppmp/costcenter', views.cc_ppmp, name='cc_ppmp'),
]