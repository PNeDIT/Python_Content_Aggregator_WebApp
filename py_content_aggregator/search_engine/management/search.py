import requests_html

ses = requests_html.HTMLSession()

def search(searchTerm, url, resultsClass, titleClass, descriptionClass, dateClass, urlClass, searchTermPos):
    url = insert(url, searchTerm, searchTermPos)
    res = ses.get(url)
    results = res.html.find(resultsClass)
    formattedResults = []
    for result in results:
        title = result.find(titleClass, first=True).text
        description = result.find(descriptionClass, first=True).text
        date = result.find(dateClass, first=True).text
        url = result.find(urlClass, first=True).absolute_links.pop()
        formattedResults.append({'title': title, 'description': description, 'date': date, 'url': url})
    return formattedResults

def insert (str, strToInsert, pos):
    return str[:pos]+strToInsert+str[pos:]