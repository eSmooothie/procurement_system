from django.urls import path

from .Category import CategoryAPI
from .CostCenter import CostCenterPPMPDetails

urlpatterns = [
    path('categories', CategoryAPI.as_view(), name="CategoryAPIsearch"),
    path('cost_center/ppmp_detail', CostCenterPPMPDetails.as_view(), name="CostCenterOrderDetailsAPIsearch"),
]
    