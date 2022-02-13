from django.shortcuts import render
from apps.objects.models import Objects
from apps.home.models import Setting

# Create your views here.
def object_index(request):
    setting = Setting.objects.get(pk = 1)
    objects = Objects.objects.all()
    context = {
        'setting' : setting, 
        'objects_index' : objects,
    }
    return render(request, 'objects/index.html', context)

def object_detail(request, id):
    object = Objects.objects.get(id = id)
    setting = Setting.objects.get(pk = 1)
    context = {
        'setting' : setting, 
        'objects_detail' : object,
    }
    return render(request, 'objects/detail.html', context)