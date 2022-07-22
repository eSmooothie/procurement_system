from django.contrib import admin

# Register your models here.
from .models import CostCenter, CostCenterUser, Ppmp, SourceOfFund

admin.site.register(CostCenter)
admin.site.register(CostCenterUser)
admin.site.register(Ppmp)
admin.site.register(SourceOfFund)