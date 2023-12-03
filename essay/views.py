from django.shortcuts import render

# Create your views here.

def essaies(request):
    context = {}
    return render(request,'essay/essay.html',context)