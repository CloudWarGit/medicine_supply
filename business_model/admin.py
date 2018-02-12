from django.contrib import admin
from business_model.models import *

# Register your models here.

for model in [Product,BusniessManager, Customer, BankAccount, Role, BMRoyaltyByMonth, CustomerPromotionByMonth]:
    admin.site.register(model)