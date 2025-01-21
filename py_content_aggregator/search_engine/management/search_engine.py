from .search import search
from .sort import sortByRelevance

from search_engine.models import Search_Sites
from search_engine.models import Searches
from search_engine.models import Forbidden_word
from search_engine.models import Forbidden_Searche

from datetime import datetime

def init(searchTerm):

    for f_word in Forbidden_word.objects.all():
        if f_word.word in searchTerm:
            f = Forbidden_Searche.objects.create(searchTerm=searchTerm, date_time=datetime.now())
            raise Exception("This search contains a forbidden word!!!")


    s = Searches.objects.create(searchTerm=searchTerm, date_time=datetime.now())
    sources = Search_Sites.objects.all()

    sortedRes = []

    for source in sources:
        sortedRes += search(searchTerm, source.url, source.results, source.title, source.description, source.date, source.url_class, source.search_term_pos)

    return sortByRelevance(sortedRes, searchTerm)