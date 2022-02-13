from django.shortcuts import render
from apps.home.models import Setting
from apps.objects.models import Objects, ObjectsImages

# Create your views here.
def index(request):
    setting = Setting.objects.get(pk = 1)
    objects = Objects.objects.all()
    context = {
        'setting' : setting, 
        'objects' : objects
    }
    return render(request, 'header-2.html', context)