from django.urls import path
from .views import IndexView, PruebaListView, TestModelListView

urlpatterns = [
    path('home/', IndexView.as_view()),
    path('lista/', PruebaListView.as_view()),
    path('test_list/', TestModelListView.as_view())
]
