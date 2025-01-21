from django.contrib import admin

from .models import Search_Sites
from .models import Searches
from .models import Forbidden_word
from .models import Forbidden_Searche

@admin.register(Search_Sites)
class Search_Sites_Admin(admin.ModelAdmin):
    list_display = ("title", "url", "date")

@admin.register(Searches)
class Searches_Admin(admin.ModelAdmin):
    list_display = ("searchTerm", "date_time")[:10]

@admin.register(Forbidden_word)
class Forbidden_word_Admin(admin.ModelAdmin):
   display = ("word")

@admin.register(Forbidden_Searche)
class Forbidden_Searche_Admin(admin.ModelAdmin):
    list_display = ("searchTerm", "date_time")

