from django.contrib import admin

# Register your models here.
from .models import Category, CostCenter, CostCenterBudget, CostCenterUser, Ppmp, SourceOfFund
from .models import OrderDetails, Item, Prices, App

admin.site.register(CostCenter)
admin.site.register(CostCenterUser)
admin.site.register(Ppmp)
admin.site.register(SourceOfFund)
admin.site.register(CostCenterBudget)
admin.site.register(Category)
admin.site.register(OrderDetails)
admin.site.register(Item)
admin.site.register(Prices)
admin.site.register(App)