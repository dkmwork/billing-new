# Generated by Django 3.2.4 on 2021-07-13 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billingapp', '0002_auto_20210710_0219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_emnail',
            new_name='user_email',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='uom_conversion',
            name='operations',
            field=models.CharField(choices=[('Addition', 'Addition'), ('Sutraction', 'Subtraction'), ('Multiplication', 'Multiplication'), ('Division', 'Division')], max_length=40),
        ),
    ]
