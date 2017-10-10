from pstore.models import QueryResult
from pstore.models import App
from pstore.models import Query
results = []
query = "Gandhi"
ans = Query.objects.filter(sterm=query)
if ans.exists():
  for m in ans.values():
    #print(m['queryresult_id'])
    results.append(QueryResult.objects.filter(id=m['queryresult_id'])[0])
    #print(results)
else:
    print("No value")
print(results)

ans1 = App.objects.filter(sterm='whatsapp')
if ans1.exists():
  results1 = ans1
print(ans1)

