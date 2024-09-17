from django.shortcuts import render, redirect   
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    product_entries = Product.objects.all()

    context = {
        'app_name' : 'Toko Messi Indah',
        'name' : 'Theodore Kevin Himawan',
        'class': 'PBP F',
        'product_name' : 'Messi Barcelona Jersey',
        'price' : '5000000',
        'description': 'A brand new Barcelona jersey of legendary player Lionel Messi',
        'category': 'Jersey',
        'product_entries': product_entries 
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product.html", context)
