from django.urls import path

from .views import ppmp_views , login_view
from .views.api import ( PpmpListApiView )

urlpatterns = [
    #auth user
    path('', login_view.login_user, name='login_user'),
    path('auth/user', login_view.auth_user, name="auth_user"),
    path('logout/', login_view.logout_user, name="logout_user"),
    #api
    # path('api/ppmp', PpmpListApiView.as_view()),
    #ppmp
    path('home/', ppmp_views.index, name='home'),
    path('home/ppmp', ppmp_views.index, name='ppmp'),
    path('home/ppmp/costcenter/<int:cc_id>/', ppmp_views.cc_ppmp, name='cc_ppmp'),
]