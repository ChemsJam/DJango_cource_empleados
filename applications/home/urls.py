from django.urls import path
from .views import IndexView, PruebaListView

urlpatterns = [
    path('home/', IndexView.as_view()),
    path('home/lista/', PruebaListView.as_view())
]
