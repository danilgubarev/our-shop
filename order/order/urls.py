"""order URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authorization_registration import views
from contact_page.views import contact_page
from main_page.views import main_page
from product_page.views import product_page
from shopping_cart_page.views import shopping_cart_page
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', views.register, name='registration'),
    path('authorization/', views.view_login, name='authorization'),
    path('', main_page, name='main'),
    path('logout/', views.user_logout, name='logout'),
    path('contact_page/', contact_page, name='contact'),
    path('product_page/', product_page, name='product'),
    path('shopping_cart_page/', shopping_cart_page, name='shopping'),


]
