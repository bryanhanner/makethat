from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from .models import UserProfile

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.:*)")

def profile(request, username):
    u = get_object_or_404(UserProfile, username=username)
    context = {
        'user_profile': u,
    }
    return render(request, 'marketplace/profile.html', context)

def gallery(request, username):
    response = "You're looking at %'s."
    return HttpResponse(response % username)

def create(request, username):
    return HttpResponse("You're creating an artwork for %s." % username)