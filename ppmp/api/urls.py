from django.urls import path

from ppmp.models import Item

from .Category import CategoryAPI
from .CostCenter import CostCenterPPMPDetails

from . import item, order_item, app, ppmp, item, stayup

urlpatterns = [
    path('categories', CategoryAPI.as_view(), name="CategoryAPIsearch"),
    path('cost_center/ppmp_detail', CostCenterPPMPDetails.as_view(), name="CostCenterOrderDetailsAPIsearch"),
    path('add/ppmp', ppmp.add_ppmp, name="add_ppmp"),
    
    path('orderitem/update', order_item.put_ppmp_orderitems, name="OrderItem"),
    path('orderitem/logs', order_item.get_orderitem_logs, name="OrderItemLogs"),
    path('orderitem/purchase_request', order_item.put_purchase_request, name="OrderItemPR"),
    path('app/get/consolidated/ppmps', app.get_consolidated_ppmp, name="get_consolidated_ppmp"),

    path('item/autocomplete_search', item.autocomplete_search, name="item_search"),
    path('item/add', item.add_item, name="add_item"),
    path('item/add/request', item.req_item, name="req_item"),
    path('item/approved/<str:item_id>', item.approved_req_item, name="approve_req_item"),
    path('item/get_request', item.get_req_item, name="get_req_item"),
    path('item/request/update', item.update_req_item, name="update_req_item"),

    #ping website to stay awake
    path('wakeup', stayup.awake, name="replit_ping")
]
    