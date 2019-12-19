from django.shortcuts import render
from django.http import HttpResponse
import operator

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def count(request):
    fulltext =request.GET['fulltext']
    bill = fulltext.split()
    worddict ={}
    for word in bill:
        if word in worddict:
            worddict[word] +=1
        else:
            worddict[word] = 1
    countedwords = sorted(worddict.items(), key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(bill), 'countedwords':countedwords})