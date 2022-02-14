from django.shortcuts import render
from apps.news.models import News
from apps.home.models import Setting

# Create your views here.
def news_index(request):
    setting = Setting.objects.get(pk = 1)
    news = News.objects.all()
    context = {
        'setting' : setting, 
        'news_index' : news,
    }
    return render(request, 'news/index.html', context)

def news_detail(request, id):
    news = News.objects.get(id=id)
    setting = Setting.objects.get(pk = 1)
    context = {
        'setting' : setting, 
        'news_detail' : news,
    }
    return render(request, 'news/detail.html', context)