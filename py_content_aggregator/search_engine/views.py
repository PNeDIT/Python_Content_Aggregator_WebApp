from django.views.generic import ListView

from .models import Search_Sites

from .management.search_engine import init

class HomePageView(ListView):
    template_name = "homepage.html"
    model = Search_Sites

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SearchView(ListView):
    template_name = "search.html"
    model = Search_Sites

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["searches"] = init(self.request.GET["query"])[:10]
        return context
