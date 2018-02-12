# Generated by Django 2.0 on 2017-12-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busniessmanager',
            name='bm_name',
            field=models.CharField(max_length=32, unique=True, verbose_name='招商经理姓名'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_name',
            field=models.CharField(max_length=32, unique=True, verbose_name='客户名字'),
        ),
    ]
