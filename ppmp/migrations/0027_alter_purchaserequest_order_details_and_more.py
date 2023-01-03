# Generated by Django 4.0.5 on 2023-01-03 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ppmp', '0026_purchaserequest_qty_purchaserequest_unit_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaserequest',
            name='order_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ppmp.orderdetails'),
        ),
        migrations.AlterField(
            model_name='requestitemcategory',
            name='req_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ppmp.requestitem'),
        ),
    ]