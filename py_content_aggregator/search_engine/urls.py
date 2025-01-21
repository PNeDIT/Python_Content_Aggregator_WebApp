from django.urls import path

from .views import HomePageView
from .views import SearchView

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("search", SearchView.as_view(), name="search"),
]
