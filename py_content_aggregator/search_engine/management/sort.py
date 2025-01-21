from fastDamerauLevenshtein import damerauLevenshtein

def sortByRelevance(results, searchTerm):
    n = len(results)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if moreSimilar(results[j]['title'], results[j+1]['title'], searchTerm):
                swapped = True
                results[j], results[j + 1] = results[j + 1], results[j]
        if not swapped:
            return results
    return results

def moreSimilar(term1, term2, searchTerm):
    return damerauLevenshtein(term1, searchTerm, similarity=True) < damerauLevenshtein(term2, searchTerm, similarity=True)