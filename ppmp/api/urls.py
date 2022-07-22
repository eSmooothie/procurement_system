from django.urls import path

from .Category import CategoryAPI

urlpatterns = [
    path('categories/search', CategoryAPI.as_view(), name="CategoryAPIsearch"),
]
    