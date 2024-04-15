from django.db import models


class Customers(models.Model):
    customer = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    
    def __str__(self):

        return self.customer + ' ' + self.name


class CustomerProducts(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product_code = models.CharField(max_length=200)
    shrimp_size = models.CharField(max_length=200)
    
    def __str__(self):

        return str(self.customer) + ' ' + self.product_code + ' ' + self.shrimp_size
