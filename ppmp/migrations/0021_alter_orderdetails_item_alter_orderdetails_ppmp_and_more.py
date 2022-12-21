# Generated by Django 4.0.5 on 2022-10-28 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ppmp', '0020_alter_orderdetails_item_alter_orderdetails_ppmp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='item', to='ppmp.item'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='ppmp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='ppmp', to='ppmp.ppmp'),
        ),
        migrations.AlterField(
            model_name='ppmptrack',
            name='orderdetails',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='ppmp.orderdetails'),
        ),
        migrations.AlterField(
            model_name='procurementmode',
            name='app',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, related_name='APP', to='ppmp.app'),
        ),
        migrations.AlterField(
            model_name='procurementmode',
            name='orderdetail',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, related_name='OrderItem', to='ppmp.orderdetails'),
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='order_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ppmp.orderdetails'),
        ),
    ]
