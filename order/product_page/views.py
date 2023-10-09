from django.shortcuts import render

# Create your views here.
def product_page(request):
    return render(request, 'product_page/product_page.html')