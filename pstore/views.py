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
def search_apps(request):
  results = []
  if request.method == 'POST':
    query = request.POST.get('query')

    ans = App.objects.filter(sterm=query)
    if ans.exists():
      results = ans
    else:
      url = 'https://play.google.com/store/search?'
      q = url + "q=" + query+"&c=apps"
      r = requests.get(q)
      soup = BeautifulSoup(r.text,"html.parser")
      s = soup.findAll('div','details')[:10]
      results = []
      results1 = []
      result = {}
      for i in s:
        i1a =  i1[0]['href']
        i1a1 = 'https://play.google.com/'+i1a
        result['link'] = i1a1
        results.append(result)
        result={}
        for j in range(10):
          link1 = results[j]['link']
          r1 = requests.get(link1)
          soup1 = BeautifulSoup(r1.text,"html.parser")
          title_div = soup1.find( 'div', {'class':'document-title'} )
          title = title_div.find( 'div' ).get_text().strip()
          subtitle = soup1.find( 'a', {'class' : 'document-subtitle primary'} )
          developer = subtitle.get_text().strip()
          dev_link = subtitle.get('href').strip()
          emaill = []
          for dev_link in soup1.find_all( 'a', {'class' : 'dev-link'} ):
            email = dev_link.get( 'href' ).strip()
            emaill.append(email)
          emailid = next((x for x in emaill if 'mailto' in x), None)
          link2 = link1.split("/")[6].split('=')[1]
          result1 = {}
          result1['AppId'] = link2
          result1['AppName'] = title
          result1['AppDeveloper'] = developer
          result1['IconURL'] = link1
          result1['DevEmail'] = emailid.split(':')[1]
          results1.append(result1)
          q3 = App()
          q3.AppId = link2
          q3.sterm=query
          q3.AppName = title
          q3.AppDeveloper = developer
          q3.DevEmail = email1[0]
          q3.IconURL = link1
          q3.save()

  return render(request, 'pstore/search_app.html',
                            {'results': results1})




