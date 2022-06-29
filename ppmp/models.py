from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    code = models.CharField(blank=True, max_length=255)
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return "Category Code:{self.code}"

class Item(models.Model):
    general_name = models.CharField(blank=True, max_length=255)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    def __str__(self):
        return "Item ID#{self.id}"

class ItemDescription(models.Model):
    specifics = models.CharField(blank=True, max_length=255)
    item = models.ForeignKey(Item, on_delete=models.RESTRICT)

    def __str__(self):
        return "ItemDescription ID#{self.id}"

class CostCenter(models.Model):
    code = models.CharField(blank=True, max_length=255)
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return "CostCenter Code:{}".format(self.code)

class CostCenterUser(models.Model):
    cc = models.ForeignKey(CostCenter, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return "#{} - CC:{} U:{}".format(self.id, self.cc.code, self.user.id)

class CostCenterBudget(models.Model):
    org_budget = models.CharField(blank=True, max_length=255)
    cc = models.ForeignKey(CostCenter, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    def __str__(self):
        return "CostCenterBudget ID#{}".format(self.id)

class SourceOfFund(models.Model):
    code = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return "SourceOfFund ID#{self.id}"

class Ppmp(models.Model):
    year = models.CharField(blank=True, max_length=255)
    type = models.CharField(blank=True, max_length=255)
    sof_num = models.ForeignKey(SourceOfFund, on_delete=models.RESTRICT)
    cc_num = models.ForeignKey(CostCenter, on_delete=models.RESTRICT)

    def __str__(self):
        return "Ppmp ID#{self.id}"
class App(models.Model):
    
    date_created = models.DateTimeField(auto_now=True)
    quarter = models.CharField(blank=True, max_length=255)
    year = models.CharField(blank=True, max_length=255)
    type = models.CharField(blank=True, max_length=255)
    group_id = models.CharField(blank=True, max_length=255)
    source_of_fund = models.ForeignKey(SourceOfFund, on_delete=models.RESTRICT)
    item_desc = models.ForeignKey(ItemDescription, on_delete=models.RESTRICT)

    def __str__(self):
        return "App ID#{self.id}"

class Prices(models.Model):
    
    price = models.CharField(blank=True, max_length=255)
    date_created = models.DateTimeField(auto_now=True)
    unit = models.CharField(blank=True, max_length=255)
    item = models.ForeignKey(ItemDescription, on_delete=models.RESTRICT)

    def __str__(self):
        return "Prices ID#{self.id}"

class OrderDetails(models.Model):
    
    item_desc = models.ForeignKey(ItemDescription, on_delete=models.RESTRICT)
    ppmp = models.ForeignKey(Ppmp, on_delete=models.RESTRICT)
    price = models.ForeignKey(Prices,on_delete=models.RESTRICT)
    app = models.ForeignKey(App,on_delete=models.RESTRICT)
    app_status = models.CharField(blank=True, max_length=255)
    received_quatation_status = models.CharField(blank=True, max_length=255)
    award_winning_bidder_status = models.CharField(blank=True, max_length=255)
    obligate_po_status = models.CharField(blank=True, max_length=255)
    served_status = models.CharField(blank=True, max_length=255)
    qr_code = models.CharField(blank=True, max_length=255)
    first_quart_quant = models.CharField(blank=True, max_length=255)
    second_quart_quant = models.CharField(blank=True, max_length=255)
    third_quart_quant = models.CharField(blank=True, max_length=255)
    fourth_quart_quant = models.CharField(blank=True, max_length=255)
    fifth_quantity = models.CharField(blank=True, max_length=255)


    def __str__(self):
        return "OrderDetails ID#{self.id}"

class PpmpTrack(models.Model):
    
    datetime = models.DateTimeField(auto_now=True)
    cc_name = models.CharField(blank=True, max_length=255)
    barcode = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return "PpmpTrack ID#{self.id}"

class PurchaseRequest(models.Model):
    specification_details = models.CharField(blank=True, max_length=255)
    purpose = models.CharField(blank=True, max_length=255)
    date_created = models.DateTimeField(auto_now=True)
    order_details = models.ForeignKey(OrderDetails, on_delete=models.RESTRICT)

    def __str__(self):
        return "PurchaseRequest ID#{self.id}"





