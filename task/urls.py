from django.urls import path
from .views import ListNewsView,SearchView


urlpatterns = [
    path('news/', ListNewsView.as_view(), name="news-all"),
    #path('searchform/', SearchView.as_view(), name="get_name")
]