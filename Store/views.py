from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import product
from .forms import productform


def homepage(request):
    all_products = product.objects.all()
    context ={"all_products": all_products}
    return render(request, "Store\index.html", context)

def detailpage(request, input_id):
    current_product = product.objects.get(id=input_id)
    context ={"current_product": current_product}
    return render(request, "Store/detail.html", context)

def createproductpage(request):
    if request.method == "POST":
        form =productform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return HttpResponse("something went wrong")
    else:
        form =productform()
    context = {"form": form}
    return render(request, "Store/create_product.html", context)