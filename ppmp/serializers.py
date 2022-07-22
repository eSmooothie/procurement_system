from rest_framework import serializers
from .models import Ppmp, Category

def required(value):
    if value is None:
        raise serializers.ValidationError('This field is required')

class PpmpSerializer(serializers.ModelSerializer):
    year = serializers.IntegerField(validators=[required])
    class Meta:
        model = Ppmp
        fields = ['year', 'type', 'sof_num', 'cc_num']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        