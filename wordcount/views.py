from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html', {"hi": "greeting", "bye": "sad"})


def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    wordcount = {}
    for word in words:
        if word in wordcount:
            # Increase Here
            wordcount[word] += 1
        else:
            # add to dict
            wordcount[word] = 1
    sortedwords = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(words), 'sortedwords': sortedwords})


def about(request):
    return render(request, 'about.html')
