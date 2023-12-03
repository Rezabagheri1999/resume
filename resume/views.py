from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'home.html', context)


def about_me(request):
    context = {}
    return render(request,"about_me.html",context)