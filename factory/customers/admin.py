# projects/admin.py

from django.contrib import admin
from customers.models import Customers, CustomerProducts

class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customers, CustomerAdmin)

admin.site.register(CustomerProducts, CustomerAdmin)