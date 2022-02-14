from django.shortcuts import render
from apps.home.models import Setting
from apps.objects.models import Objects, ObjectsImages

# Create your views here.
def index(request):
    setting = Setting.objects.get(pk = 1)
    last_objects = Objects.objects.all().order_by('-created')[:4]
    context = {
        'setting' : setting, 
        'last_objects' : last_objects
    }
    return render(request, 'index.html', context)