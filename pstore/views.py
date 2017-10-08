from django.shortcuts import render,HttpResponse
import json
import requests
from bs4 import BeautifulSoup
from pstore.models import QueryResult

def test(request):
	return HttpResponse("test Successful!")

def search_results(request):
  results = []
  if request.method == 'POST':
    query = request.POST.get('query')

    ans = QueryResult.objects.filter(sterm=query)
    if ans.exists():
      results = ans
    else:
      url = 'https://play.google.com/store/search?'
      q = url + "q=" + query
      r = requests.get(q)
      soup = BeautifulSoup(r.text,"html.parser")

      #s = soup.findAll('a','card-click-target')
      s = soup.findAll('div','details')[:10]
      result = {}
      for i in s:
        i1 = i.findAll('a','title')
        i1a =  i1[0]['href']
        i1a1 = 'https://play.google.com/'+i1a 
        i1b = i1[0]['title']
        i1c = i1a.split("/")[2]
        q2 = QueryResult()
        q2.sterm=query
        q2.category = i1c
        q2.title = i1b
        q2.link = i1a1
        q2.save()
        result['category'] = i1c
        result['title'] = i1b
        result['link'] = i1a1
        results.append(result)
        result = {}

  return render(request, 'pstore/search_results.html',
                            {'results': results})



