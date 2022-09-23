from django.urls import path

from .Category import CategoryAPI
from .CostCenter import CostCenterPPMPDetails

from . import order_item

urlpatterns = [
    path('categories', CategoryAPI.as_view(), name="CategoryAPIsearch"),
    path('cost_center/ppmp_detail', CostCenterPPMPDetails.as_view(), name="CostCenterOrderDetailsAPIsearch"),
    path('orderitem/update', order_item.update_ppmp_orderitems, name="OrderItem"),
]
    