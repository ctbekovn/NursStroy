from django.urls import path 
from apps.objects.views import object_index, object_detail


urlpatterns = [
    path('', object_index, name = "object_index"),
    path('<int:id>/', object_detail, name = "object_detail")
]