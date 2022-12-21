import logging
from math import ceil
from unicodedata import category
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import Q
import re

from ..helper import *
from ..models import Item, RequestItem

logger = logging.getLogger("file_log")

from babel.numbers import format_currency
from datetime import date

selected_app = "item"


# Select Cost Center
@login_required(login_url='login_user')
def index(request):        

    user_fn = request.user.first_name if request.user.first_name is not None else "No Name"
    is_admin = request.user.is_staff

    selected_page = int(request.GET['page']) if 'page' in request.GET else 1
    search_keyword = request.GET['keyword'] if 'keyword' in request.GET else ""
    
    limit=50
    offset= (selected_page - 1) * limit
    
    filter_item = []
    #search_queries
    
    filter_item.append(
        Q(name__icontains=search_keyword)
    )
    
    ttl_items = Item.objects.filter(*filter_item).all().count()
    
    no_pages = ceil(ttl_items / limit)
    
    items = Item.objects.filter(*filter_item).order_by('name').all()[offset:offset + limit]
    
    unapproved_req_item = RequestItem.objects.filter(is_approved=False).all().count()

    context = page_context(
        user_fn = user_fn,
        is_admin=is_admin,
        selected_app=selected_app,
        items = items,
        selected_page=selected_page,
        search_keyword=search_keyword,
        unapproved_req_item = unapproved_req_item,
        no_pages=[i for i in range(1,no_pages)] if no_pages > 1 else [1],
    )

    return render(
        request=request, 
        template_name='item/dashboard.html' if selected_app else 'ppmp/welcome.html', 
        context=context
     )

def req_item(request):
    user_fn = request.user.first_name if request.user.first_name is not None else "No Name"
    is_admin = request.user.is_staff

    selected_page = int(request.GET['page']) if 'page' in request.GET else 1
    search_keyword = request.GET['keyword'] if 'keyword' in request.GET else ""
    
    limit=50
    offset= (selected_page - 1) * limit
    
    filter_item = []
    #search_queries
    
    filter_item.append(
        Q(name__icontains=search_keyword),
    )
    
    ttl_items = RequestItem.objects.filter(*filter_item).all().count()
    
    no_pages = ceil(ttl_items / limit)
    
    items = RequestItem.objects.filter(*filter_item).order_by('is_approved', 'created_at').all()[offset:offset + limit]

    context = page_context(
        user_fn = user_fn,
        is_admin=is_admin,
        selected_app=selected_app,
        items = items,
        selected_page=selected_page,
        search_keyword=search_keyword,
        no_pages=[i for i in range(1,no_pages)] if no_pages > 1 else [1],
    )

    return render(
        request=request, 
        template_name='item/req_item.html' if selected_app else 'ppmp/welcome.html', 
        context=context
     )


def single_item(request, item_id):
    user_fn = request.user.first_name if request.user.first_name is not None else "No Name"
    is_admin = request.user.is_staff

    item = Item.objects.get(id=item_id)
    
    context = page_context(
        user_fn = user_fn,
        is_admin=is_admin,
        selected_app=selected_app,
        item=item,
    )

    return render(
        request=request, 
        template_name='item/per_item.html' if selected_app else 'ppmp/welcome.html', 
        context=context
     )


