from django.shortcuts import render

# Create your views here.
def authorization_page(request):
    return render(request, 'authorization_registration/authorization.html')

def registration_page(request):
    return render(request, 'authorization_registration/registration.html')