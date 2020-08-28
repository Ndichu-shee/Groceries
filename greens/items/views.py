from django.shortcuts import render



def home(request):
    return render(request, 'products/home.html')

def stock(request):
    return render(request, 'products/stock.html')

