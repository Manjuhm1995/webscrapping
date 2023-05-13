from django.urls import path
from .views import scrape_news

urlpatterns = [
    path('scrape/', scrape_news, name='scrape_news'),
]
