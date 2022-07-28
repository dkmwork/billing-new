# Generated by Django 3.2.4 on 2021-11-24 03:20

import billingapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billingapp', '0009_purchase_items_returns_bridge_purchase_returns_purchase_returns_gst_wise_warehouse_bin_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_shortname',
            field=models.CharField(blank=True, max_length=5, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='contact_no',
            field=models.CharField(max_length=40, validators=[billingapp.models.validate_mobileno], verbose_name='Mobile No'),
        ),
        migrations.AlterField(
            model_name='state',
            name='state_code',
            field=models.CharField(max_length=2, unique=True, verbose_name='State Code'),
        ),
    ]
