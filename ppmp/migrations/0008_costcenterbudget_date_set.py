# Generated by Django 4.0.5 on 2022-07-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppmp', '0007_costcenterbudget_curr_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='costcenterbudget',
            name='date_set',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]