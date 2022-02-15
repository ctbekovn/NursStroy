from django.shortcuts import render
from apps.home.models import Setting
from apps.objects.models import Objects, ObjectsImages
from apps.news.models import News
from apps.reviews.models import Rewiew

# Create your views here.
def index(request):
    setting = Setting.objects.get(pk = 1)
    last_objects = Objects.objects.all().order_by('-created')[:4]
    news = News.objects.all()[:4]
    resent_news = News.objects.all().order_by('-created', )[:2]
    reviews = Rewiew.objects.all()
    context = {
        'setting' : setting, 
        'last_objects' : last_objects,
        'news' : news,
        'resent_news' : resent_news,
        'reviews' : reviews,
    }
    return render(request, 'index.html', context)
