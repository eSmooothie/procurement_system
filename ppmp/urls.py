from re import template
from django.urls import path

from ppmp.views import app_views

from .views import ppmp_views ,login_view, pdf_view
from .api.Category import CategoryAPI

urlpatterns = [
    path('home/', ppmp_views.index, name='home'),
    #auth user
    path('', login_view.login_user, name='login_user'),
    path('auth/user', login_view.auth_user, name="auth_user"),
    path('logout/', login_view.logout_user, name="logout_user"),
    #ppmp
    path('home/ppmp', ppmp_views.index, name='ppmp'),
    path('home/ppmp/costcenter/<int:cc_id>/', ppmp_views.cc_ppmp, name='cc_ppmp'),
    #app
    path('home/app', app_views.index, name='app'),
    #pdf
    path('pdf/download/ppmp', pdf_view.create_ppmp_doc, name='generate_pdf'),
]