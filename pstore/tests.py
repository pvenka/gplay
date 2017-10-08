from django.test import TestCase
from django.test import Client
# Create your tests here.


class ViewTests(TestCase):
  def testTestView(self):
    resp = self.client.get('/pstore/test/')
    self.assertEqual(resp.status_code, 200)
  
  def testSearch(self):
    resp = self.client.post('/pstore/search_results/', {'query': 'Gandhi'} )
    self.assertEqual(resp.status_code, 200)
  
  def testSearchContent(self):
    resp = self.client.post('/pstore/search_results/', {'query': 'Gandhi'} )
    self.assertNotEqual(resp.content, '')
