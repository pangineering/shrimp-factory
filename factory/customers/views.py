from django.http import HttpResponse
from django.shortcuts import render
from customers.models import Customers, CustomerProducts

def index(request):
    customers = Customers.objects.all()
    context = {

        "customers": customers

    }
    return render(request, "index.html", context)

def products(request, pk):
    customer = Customers.objects.get(pk=pk)
    products = CustomerProducts.objects.get(customer=customer.pk)

    context = {

        "customer": customer,
        "products": products

    }
    return render(request, "products.html", context)