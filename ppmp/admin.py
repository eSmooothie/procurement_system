from django.contrib import admin

# Register your models here.
from .models import CostCenter, CostCenterUser

admin.site.register(CostCenter)
admin.site.register(CostCenterUser)