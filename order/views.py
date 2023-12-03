from django.shortcuts import render

# Create your views here.

def orders(request):
    context = {}
    return render(request, "order/order.html",context)