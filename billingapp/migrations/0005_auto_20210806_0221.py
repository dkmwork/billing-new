# Generated by Django 3.2.4 on 2021-08-06 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billingapp', '0004_auto_20210715_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_items_bridge',
            name='item_hsncode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='purchase_items_bridge',
            name='uom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='purchase_items_bridge', to='billingapp.uom'),
        ),
    ]
