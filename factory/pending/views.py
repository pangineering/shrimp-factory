from django.http import HttpResponse
from django.shortcuts import render

def pending_index(request):
    return render(request, "pending_index.html", {})
