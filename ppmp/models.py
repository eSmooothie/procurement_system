from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

from babel.numbers import format_currency
class Category(models.Model):
    code = models.CharField(blank=True, max_length=255)
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return "cat_id:{}-{}".format(self.id, self.name)

class Item(models.Model):
    name = models.CharField(blank=True, max_length=255)
    unit = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return "item_id:{}-{}".format(self.id,self.name)

    def get_price(self, datetime = None):
        # retrieve a specific price
        if datetime and Prices.objects.filter(item_id=self.id, created_at__year=datetime.year).exists():
            price = Prices.objects.filter(item_id=self.id, created_at__year=datetime.year).get()
            return price.price
        elif Prices.objects.filter(item_id=self.id).order_by('-id').exists(): # retrieve the latest date
            price = Prices.objects.filter(item_id=self.id).order_by('-id').get()
            return price.price
        return -1

    @property
    def curr_price(self):
        price_obj = Prices.objects.filter(item=self).order_by('-id').first()
        if price_obj:
            price = format_currency(price_obj.price, 'PHP', locale="en_US")
        else:
            price = None

        return price

    @property
    def prev_price(self):
        try:
            price_obj = Prices.objects.filter(item=self).order_by('-id').all()[1]
            price = format_currency(price_obj.price, 'PHP', locale="en_US"),
        except IndexError:
            price = None

        return price

    @property
    def categories(self):
        return ItemCategory.objects.filter(item=self).all()

class ItemCategory(models.Model):
    item = models.ForeignKey(Item, blank=True, on_delete= models.RESTRICT, null=True)
    cat_code = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return f'''Item: {self.item.name }\nCode:{self.cat_code}'''

    @property
    def category(self):
        return Category.objects.get(code=self.cat_code)
        
class Prices(models.Model):
    
    item = models.ForeignKey(Item, on_delete=models.RESTRICT, null=True)
    price = models.CharField(blank=True, max_length=255)    
    created_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "price_id:{}-Item:{}-{}".format(self.id, self.item, self.price)
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
    cc = models.ForeignKey(CostCenter, on_delete=models.RESTRICT, null=True)
    cat = models.ForeignKey(Category, on_delete=models.RESTRICT, null=True)
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
    sof = models.ForeignKey(SourceOfFund, blank=True, on_delete=models.RESTRICT)
    cc_code = models.CharField(blank=True, max_length=255)

    @property
    def cost_center(self):
        return CostCenter.objects.get(code=self.cc_code)

    @property
    def has_purchase_request(self):
        """return True if any of the ordered item has purchased request otherwise false"""
        ordereditems = OrderDetails.objects.filter(ppmp=self).all()
        for item in ordereditems:
            if item.purchase_request is not None:
                return True
        return False

    def __str__(self):
        return "ppmp_id:{}-{}".format(self.id, self.year)

    
class App(models.Model):
    
    created_at = models.DateTimeField(auto_now=True)
    quarter = models.CharField(blank=True, max_length=255)
    year = models.CharField(blank=True, max_length=255)
    type = models.CharField(blank=True, max_length=255)
    group_id = models.CharField(blank=True,null=True, max_length=255)
    sof = models.ForeignKey(SourceOfFund, on_delete=models.RESTRICT)
    
    def __str__(self):
        return "app_id:{}-{}".format(self.id, self.year)



class OrderDetails(models.Model):
    
    ppmp = models.ForeignKey(Ppmp,null=True, on_delete=models.RESTRICT, related_name="ppmp")
    item = models.ForeignKey(Item, null=True, on_delete=models.RESTRICT, related_name="item")
    cat_code = models.CharField(blank=True,null=True, max_length=255)

    app_status = models.CharField(blank=True,null=True, max_length=255)
    received_quotation_status = models.CharField(blank=True,null=True, max_length=255)
    award_winning_bidder_status = models.CharField(blank=True,null=True, max_length=255)
    obligate_po_status = models.CharField(blank=True,null=True, max_length=255)
    served_status = models.CharField(blank=True,null=True, max_length=255)

    first_quant = models.CharField(blank=True,null=True, max_length=255)
    second_quant = models.CharField(blank=True,null=True, max_length=255)
    third_quant = models.CharField(blank=True,null=True, max_length=255)
    fourth_quant = models.CharField(blank=True,null=True, max_length=255)

    code = models.CharField(blank=True,null=True, max_length=255)
    created_at = models.CharField(blank=True, null=True, max_length=255)
    
    @property
    def compute_amnt(self):
        price = float(self.get_current_price)
        quarter_amnt = (
            float(self.first_quant) * price,
            float(self.second_quant) * price,
            float(self.third_quant) * price,
            float(self.fourth_quant) * price,
        )
        return quarter_amnt

    @property
    def compute_amnt_formatted(self):
        amnt = self.compute_amnt
        return (
            format_currency(amnt[0], 'PHP', locale="en_US"),
            format_currency(amnt[1], 'PHP', locale="en_US"),
            format_currency(amnt[2], 'PHP', locale="en_US"),
            format_currency(amnt[3], 'PHP', locale="en_US")
        )

    @property
    def get_current_price(self):
        dt = datetime(year=int(self.ppmp.year), month=1, day=1)
        price = self.item.get_price(datetime=dt)
        return price

    @property
    def get_current_price_formatted(self):
        return format_currency(self.get_current_price, 'PHP', locale="en_US")

    @property
    def get_costcenter(self):
        cc_code = self.ppmp.cc_code
        cc = CostCenter.objects.get(code=cc_code)
        return cc

    @property
    def purchase_request(self):
        if PurchaseRequest.objects.filter(order_details=self).exists():
            return PurchaseRequest.objects.get(order_details=self)
        else:
            return None

    def __str__(self):
        return "orddetails_id:{}".format(self.id)

class ProcurementMode(models.Model):
    orderdetail = models.ForeignKey(OrderDetails, blank=True, related_name = "OrderItem", on_delete=models.CASCADE)
    app = models.ForeignKey(App, null=True, blank=True, related_name = "APP", on_delete=models.RESTRICT)
    mode = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return f'''{self.orderdetail.id} - {self.app} [{self.mode}]'''
class PpmpTrack(models.Model):
    orderdetails = models.ForeignKey(OrderDetails,null=True, on_delete=models.CASCADE)
    datetime = models.CharField(blank=True,null=True, max_length=255)
    cc_name = models.CharField(blank=True,null=True, max_length=255)
    barcode = models.CharField(blank=True,null=True, max_length=255)

    def __str__(self):
        return "ppmptrack_id:{}".format(self.id)

class PurchaseRequest(models.Model):
    specification_details = models.CharField(blank=True,null=True, max_length=255)
    purpose = models.CharField(blank=True,null=True, max_length=255)
    unit_cost = models.CharField(blank=True,null=True, max_length=255)
    qty = models.IntegerField(blank=True,null=True)
    date_created = models.DateTimeField(auto_now=True)
    order_details = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)

    def __str__(self):
        return "purchreq_id:{}".format(self.id)

class RequestItem(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
    name = models.CharField(blank=True, max_length=255)
    unit = models.CharField(blank=True, max_length=255)
    price = models.CharField(blank=True, max_length=255)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "ReqItem(id={},user={},name={})".format(self.id, self.user.email, self.name)

    @property
    def formatted_price(self):
        return format_currency(self.price, 'PHP', locale="en_US")

    @property
    def categories(self):
        return RequestItemCategory.objects.filter(req_item=self).all()

    def delete_categories(self):
        RequestItemCategory.objects.filter(req_item=self).all().delete()

class RequestItemCategory(models.Model):
    req_item = models.ForeignKey(RequestItem, null=True, on_delete=models.CASCADE)
    cat_code = models.CharField(blank=True, max_length=255)

    @property
    def category(self):
        return Category.objects.get(code=self.cat_code)





