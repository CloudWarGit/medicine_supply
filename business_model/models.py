from django.db import models
from django.urls import reverse

# Create your models here.

class Product (models.Model):
    product_name = models.CharField("商品名", max_length=100, unique=True)
    common_name = models.CharField("通用名", max_length=100, blank=True)
    specification = models.CharField("规格", max_length=100, blank=True)
    price = models.DecimalField("挂网价", max_digits=10, decimal_places=2, blank=True)
    medicare = models.BooleanField("医保")
    product_factory = models.CharField("生产厂家", max_length=150, blank=True)
    symptoms = models.CharField("适应症", max_length=500)
    present_business = models.CharField("配送商业", max_length=500, blank=True)
    
    def __str__(self):
        return self.product_name 
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})
    
class Role(models.Model):
    variety_name = models.CharField("品种", max_length=100)
    phone = models.IntegerField("电话", blank=True)
    email = models.EmailField("邮箱", blank=True)
    bank_account = models.ForeignKey("BankAccount", on_delete=models.CASCADE)
    
class BusniessManager(Role):
    bm_name = models.CharField("招商经理姓名", max_length=32, unique=True)
    product_name = models.ManyToManyField("Product", verbose_name="产品名称", related_name="bm_name")
    royalty_unit = models.DecimalField("提成金额（元/盒）", max_digits=10, decimal_places=2,)   
    
    def __str__(self):
        return self.bm_name
    
    def get_absolute_url(self):
        return reverse('bm_detail', kwargs={'pk': self.pk})

class Customer(Role):
    customer_name = models.CharField("客户名字", max_length=32, unique=True)
    product_name = models.ManyToManyField("Product", verbose_name="产品名称", related_name="customer_name")
    academic_promotion_unit = models.DecimalField("学术推广费（元/盒）", max_digits=10, decimal_places=2,)
    
    def __str__(self):
        return self.customer_name
    
    def get_absolute_url(self):
        return reverse('customer_detail', kwargs={'pk': self.pk})

class BankAccount(models.Model):
    account = models.IntegerField("银行账号", unique=True)
    account_holder = models.CharField("开户人", max_length=32)
    account_address = models.CharField("开户行", max_length=100)
    
    def __str__(self):
        return self.account_holder
    
class BMRoyaltyByMonth(models.Model):
    date = models.DateField("结算日")
    bm_name = models.ForeignKey("BusniessManager", on_delete=models.CASCADE, verbose_name="招商经理", related_name="royalty_by_month")
    royalty_amount = models.DecimalField("提成总额", max_digits=10, decimal_places=2,)
    
    def __str__(self):
        return "{}_{}_{}".format(self.bm_name,self.royalty_amount,self.date)
        
class CustomerPromotionByMonth(models.Model):
    date = models.DateField("结算日")
    customer_name = models.ForeignKey("Customer", on_delete=models.CASCADE, verbose_name="客户", related_name="promotion_by_month")
    academic_promotion_amount = models.DecimalField("推广费总额", max_digits=10, decimal_places=2,)
    
    def __str__(self):
        return "{}_{}_{}".format(self.customer_name,self.academic_promotion_amount,self.date)
    