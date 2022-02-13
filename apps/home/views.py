from django.shortcuts import render
from apps.home.models import Setting

# Create your views here.
def index(request):
    return render(request, 'header-2.html')