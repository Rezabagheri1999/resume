from django.shortcuts import render


# Create your views here.

def contact_me(request):
    context = {}
    return render(request, 'contact/contact.html')
