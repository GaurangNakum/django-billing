from django.shortcuts import render
from django.shortcuts import HttpResponse
from store.models.product import Product


def product_get(request):
    product = Product.objects.all()
    return render(request,'productmaster.html',{'product' : product})

def product_search(request):
    search_product = request.POST['src_prod_name']
    product = Product.objects.filter(name__icontains=search_product)
    return render(request,'productmaster.html',{'product' : product})

