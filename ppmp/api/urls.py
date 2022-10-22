from django.urls import path

from .Category import CategoryAPI
from .CostCenter import CostCenterPPMPDetails
from .Item import ItemAPI

from . import order_item, app

urlpatterns = [
    path('categories', CategoryAPI.as_view(), name="CategoryAPIsearch"),
    path('cost_center/ppmp_detail', CostCenterPPMPDetails.as_view(), name="CostCenterOrderDetailsAPIsearch"),
    path('orderitem/update', order_item.update_ppmp_orderitems, name="OrderItem"),
    path('orderitem/logs', order_item.get_orderitem_logs, name="OrderItemLogs"),
    path('app/get/consolidated/ppmps', app.get_consolidated_ppmp, name="get_consolidated_ppmp"),
    path('items', ItemAPI.as_view(), name="ItemAPIsearch"),
]
    