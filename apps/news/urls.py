from django.urls import path 
from apps.news.views import news_index, news_detail


urlpatterns = [
    path('', news_index, name = "news_index"),
    path('<int:id>/', news_detail, name = "news_detail")
]