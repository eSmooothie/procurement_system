# Generated by Django 4.0.5 on 2023-01-03 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ppmp', '0027_alter_purchaserequest_order_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ppmptrack',
            name='orderdetails',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ppmp.orderdetails'),
        ),
        migrations.AlterField(
            model_name='procurementmode',
            name='orderdetail',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='OrderItem', to='ppmp.orderdetails'),
        ),
    ]