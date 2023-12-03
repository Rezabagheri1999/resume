from django.shortcuts import render


# Create your views here.

def social_network(request):
    context = {}
    return render(request, "social/social_posts.html", context)
