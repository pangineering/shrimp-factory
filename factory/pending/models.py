from django.db import models
from customers.models import Customers

class Pending(models.Model):
    
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product_code = models.CharField(max_length=200)
    shipment = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    packing_carton = models.CharField(max_length=200)
    pieces_packing = models.CharField(max_length=200)
    remaining_orders = models.CharField(max_length=200)
    stock_srt = models.CharField(max_length=200)
    stock_jwd = models.CharField(max_length=200)
    srt11 = models.CharField(max_length=200)
    srt12 = models.CharField(max_length=200)
    srt13 = models.CharField(max_length=200)
    srt14 = models.CharField(max_length=200)
    srt2 = models.CharField(max_length=200)
    srt3 = models.CharField(max_length=200)
    total_stock = models.CharField(max_length=200)
    balance_stock = models.CharField(max_length=200)
    rm_pending = models.CharField(max_length=200)
    
    def __str__(self):

        return str(self.customer) + ' ' + self.product_code + ' ' + self.shipment + ' ' + self.rm_pending

