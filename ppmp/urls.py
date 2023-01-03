from re import template
from django.urls import path

from ppmp.views import app_views

from .views import ppmp_views ,login_view, pdf_view, item_view
from .api.Category import CategoryAPI

urlpatterns = [
    path('home/', ppmp_views.dashboard, name='home'),
    #auth user
    path('', login_view.login_user, name='login_user'),
    path('auth/user', login_view.auth_user, name="auth_user"),
    path('logout/', login_view.logout_user, name="logout_user"),
    #ppmp
    path('home/ppmp', ppmp_views.index, name='ppmp'),
    path('home/ppmp/costcenter/<str:cc_code>/', ppmp_views.cc_ppmp, name='cc_ppmp'),
    path('home/ppmp/costcenter/ppmp/<int:ppmp_id>', ppmp_views.ppmp_detail, name="ppmp_details"),
    path('home/ppmp/costcenter/ppmp/<int:ppmp_id>/<str:cat_code>/log', ppmp_views.view_logs, name="view_logs"),
    path('home/ppmp/costcenter/ppmp/<int:ppmp_id>/<str:cat_code>/<int:orderitem_id>/purchase_request', ppmp_views.view_pr, name="view_pr"),
    #app
    path('home/app', app_views.index, name='app'),
    #item
    path('home/item', item_view.index, name='item'),
    path('home/requested/item', item_view.req_item, name='req_item_view'),
    path('home/item/<str:item_id>', item_view.single_item, name='single_item'),
    #pdf
    path('pdf/download/ppmp/<str:cc_code>/<int:ppmp_id>/<str:cat_code>', pdf_view.create_ppmp_doc, name='generate_ppmp_pdf'),
    path('pdf/download/pr/<int:ppmp_id>/<str:cat_code>', pdf_view.create_pr_doc, name='generate_pr_pdf'),
]