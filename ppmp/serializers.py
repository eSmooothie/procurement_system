from rest_framework import serializers
from .models import App, CostCenter, CostCenterBudget, Item, ItemCategory, OrderDetails, Ppmp, Category, Prices

def required(value):
    if value is None:
        raise serializers.ValidationError('This field is required')

class PpmpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ppmp
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class CostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        fields = '__all__'

class APPSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = App
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemCategorySerializer( serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    class Meta:
        model = ItemCategory
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    class Meta:
        model = Prices
        fields = '__all__'

class OrderDetailsSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    ppmp = PpmpSerializer(read_only=True)
    price = PriceSerializer(read_only=True)
    class Meta:
        model = OrderDetails
        fields = '__all__'



class CCBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenterBudget
        fields = '__all__'
        