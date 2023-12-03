from django.shortcuts import render


# Create your views here.

def projects(request):
    context = {}
    return render(request, 'projects/projects.html', context)
