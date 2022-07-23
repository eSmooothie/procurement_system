from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    code = models.CharField(blank=True, max_length=255)
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return "cat_id:{}-{}".format(self.id, self.name)

class Item(models.Model):
    general_name = models.CharField(blank=True, max_length=255)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    def __str__(self):
        return "item_id:{}-{}".format(self.id,self.general_name)

class ItemDescription(models.Model):
    spec_1 = models.CharField(blank=True, max_length=255)
    spec_2 = models.CharField(blank=True, max_length=255)
    spec_3 = models.CharField(blank=True, max_length=255)
    spec_4 = models.CharField(blank=True, max_length=255)
    spec_5 = models.CharField(blank=True, max_length=255)
    item = models.ForeignKey(Item, on_delete=models.RESTRICT)

    def __str__(self):
        return "itemdesc_id:{}".format(self.id)

class CostCenter(models.Model):
    code = models.CharField(blank=True, max_length=255)
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return "cc_id:{}-{}".format(self.id, self.name)

class CostCenterUser(models.Model):
    cc = models.ForeignKey(CostCenter, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return "ccuser_id{}-CC:{}-U:{}".format(self.id, self.cc.name, self.user.id)

class CostCenterBudget(models.Model):
    org_budget = models.CharField(blank=True, max_length=255)
    date_set = models.DateTimeField(blank=True, null=True)
    cc = models.ForeignKey(CostCenter, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    curr_budget = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return "ccbudget_id:{}".format(self.id)

class SourceOfFund(models.Model):
    code = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return "sof_id:{}-{}".format(self.id, self.description)

class Ppmp(models.Model):
    year = models.CharField(blank=True, max_length=255)
    type = models.CharField(blank=True, max_length=255)
    sof = models.ForeignKey(SourceOfFund, on_delete=models.RESTRICT)
    cc = models.ForeignKey(CostCenter, on_delete=models.RESTRICT)

    def __str__(self):
        return "ppmp_id:{}-{}".format(self.id, self.year)
class App(models.Model):
    
    date_created = models.DateTimeField(auto_now=True)
    quarter = models.CharField(blank=True, max_length=255)
    year = models.CharField(blank=True, max_length=255)
    type = models.CharField(blank=True, max_length=255)
    group_id = models.CharField(blank=True,null=True, max_length=255)
    source_of_fund = models.ForeignKey(SourceOfFund, on_delete=models.RESTRICT)
    item_desc = models.ForeignKey(ItemDescription, on_delete=models.RESTRICT)

    def __str__(self):
        return "app_id:{}-{}".format(self.id, self.year)

class Prices(models.Model):
    
    price = models.CharField(blank=True, max_length=255)
    date_created = models.DateTimeField(auto_now=True)
    unit = models.CharField(blank=True, max_length=255)
    item = models.ForeignKey(ItemDescription, on_delete=models.RESTRICT)

    def __str__(self):
        return "price_id:{}-Item:{}-{}",format(self.id, self.item, self.price)

class OrderDetails(models.Model):
    
    item_desc = models.ForeignKey(ItemDescription, on_delete=models.RESTRICT)
    ppmp = models.ForeignKey(Ppmp,null=True, on_delete=models.RESTRICT)
    price = models.ForeignKey(Prices,null=True,on_delete=models.RESTRICT)
    app = models.ForeignKey(App,null=True,on_delete=models.RESTRICT)
    app_status = models.CharField(blank=True,null=True, max_length=255)
    received_quotation_status = models.CharField(blank=True,null=True, max_length=255)
    award_winning_bidder_status = models.CharField(blank=True,null=True, max_length=255)
    obligate_po_status = models.CharField(blank=True,null=True, max_length=255)
    served_status = models.CharField(blank=True,null=True, max_length=255)
    qr_code = models.CharField(blank=True,null=True, max_length=255)
    first_quart_quant = models.CharField(blank=True,null=True, max_length=255)
    second_quart_quant = models.CharField(blank=True,null=True, max_length=255)
    third_quart_quant = models.CharField(blank=True,null=True, max_length=255)
    fourth_quart_quant = models.CharField(blank=True,null=True, max_length=255)
    date = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return "orddetails_id:{}".format(self.id)

class PpmpTrack(models.Model):
    orderdetails = models.ForeignKey(OrderDetails,null=True, on_delete=models.RESTRICT)
    datetime = models.CharField(blank=True,null=True, max_length=255)
    cc_name = models.CharField(blank=True,null=True, max_length=255)
    barcode = models.CharField(blank=True,null=True, max_length=255)

    def __str__(self):
        return "ppmptrack_id:{}".format(self.id)

class PurchaseRequest(models.Model):
    specification_details = models.CharField(blank=True, max_length=255)
    purpose = models.CharField(blank=True, max_length=255)
    date_created = models.DateTimeField(auto_now=True)
    order_details = models.ForeignKey(OrderDetails, on_delete=models.RESTRICT)

    def __str__(self):
        return "purchreq_id:{}".format(self.id)





