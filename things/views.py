from django.shortcuts import render
from .models import Thing

def home(request):
    things = Thing.objects.all()
    return render(request, 'home.html', {'things': things})
