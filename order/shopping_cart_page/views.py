from django.shortcuts import render

# Create your views here.

def shopping_cart_page(request):
    return render(request, 'shopping_cart_page/shopping_cart_page.html')