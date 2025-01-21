from django.db import models

import json

# Create your models here.
class Search_Sites(models.Model):
    url = models.URLField()
    results = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    url_class = models.CharField(max_length=50)
    search_term_pos = models.IntegerField()

    def __str__(self) -> str:
        return json.dumps({'url':self.url,
            'resultsClass':self.results,
            'titleClass':self.title,
            'descriptionClass':self.description,
            'dateClass':self.date,
            'urlClass':self.url_class,
            'searchTermPos':self.search_term_pos
            })


class Searches(models.Model):
    searchTerm = models.CharField(max_length=250)
    date_time = models.DateTimeField()

class Forbidden_word(models.Model):
    word = models.CharField(max_length=50)

class Forbidden_Searche(models.Model):
    searchTerm = models.CharField(max_length=250)
    date_time = models.DateTimeField()