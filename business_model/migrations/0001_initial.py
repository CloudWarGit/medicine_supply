# Generated by Django 2.0 on 2017-12-23 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.IntegerField(unique=True, verbose_name='银行账号')),
                ('account_holder', models.CharField(max_length=32, verbose_name='开户人')),
                ('account_address', models.CharField(max_length=100, verbose_name='开户行')),
            ],
        ),
        migrations.CreateModel(
            name='BMRoyaltyByMonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='结算日')),
                ('royalty_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='提成总额')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPromotionByMonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='结算日')),
                ('academic_promotion_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='推广费总额')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, unique=True, verbose_name='商品名')),
                ('common_name', models.CharField(blank=True, max_length=100, verbose_name='通用名')),
                ('specification', models.CharField(blank=True, max_length=100, verbose_name='规格')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='挂网价')),
                ('medicare', models.BooleanField(verbose_name='医保')),
                ('product_factroy', models.CharField(blank=True, max_length=150, verbose_name='生产厂家')),
                ('symptoms', models.CharField(max_length=500, verbose_name='适应症')),
                ('present_business', models.CharField(blank=True, max_length=500, verbose_name='配送商业')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variety_name', models.CharField(max_length=100, verbose_name='品种')),
                ('phone', models.IntegerField(blank=True, verbose_name='电话')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='邮箱')),
            ],
        ),
        migrations.CreateModel(
            name='BusniessManager',
            fields=[
                ('role_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='business_model.Role')),
                ('bm_name', models.CharField(max_length=32, verbose_name='招商经理姓名')),
                ('royalty_unit', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='提成金额（元/盒）')),
                ('product_name', models.ManyToManyField(related_name='bm_name', to='business_model.Product', verbose_name='产品名称')),
            ],
            bases=('business_model.role',),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('role_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='business_model.Role')),
                ('customer_name', models.CharField(max_length=32, verbose_name='客户名字')),
                ('academic_promotion_unit', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='学术推广费（元/盒）')),
                ('product_name', models.ManyToManyField(related_name='customer_name', to='business_model.Product', verbose_name='产品名称')),
            ],
            bases=('business_model.role',),
        ),
        migrations.AddField(
            model_name='role',
            name='bank_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business_model.BankAccount'),
        ),
        migrations.AddField(
            model_name='customerpromotionbymonth',
            name='customer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotion_by_month', to='business_model.Customer', verbose_name='客户'),
        ),
        migrations.AddField(
            model_name='bmroyaltybymonth',
            name='bm_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='royalty_by_month', to='business_model.BusniessManager', verbose_name='招商经理'),
        ),
    ]