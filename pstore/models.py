from django.db import models

# Create your models here.

class QueryResult(models.Model):
	 
  category = models.CharField(
         max_length=255,
	)
  title = models.CharField(
	 max_length=255,
	)
  link = models.URLField(
  	 max_length=255,
	)

def __str__(self):
	return ' '.join([
	  self.category,
	  self.title,
	  self.link,
	])
class Query(models.Model):
     sterm = models.CharField(
           max_length=255,
	)
     queryresult = models.ForeignKey(QueryResult, on_delete=models.CASCADE)
def __str__(self):
	return self.sterm

class App(models.Model):
  AppId = models.CharField(
            max_length=255)
  AppName = models.CharField(
            max_length=255)
  AppDeveloper = models.CharField(
            max_length=255)
  DevEmail = models.EmailField(
            max_length=254)
  IconURL = models.URLField(
            max_length=200)

def __str__(self):
       return ' '.join([
         self.AppId,
         self.AppName,
         self.AppDeveloper,
         self.DevEmail,
         self.IconURL,
	])

class AppQuery(models.Model):
     sterm = models.CharField(
           max_length=255,
        )
     app = models.ForeignKey(App, on_delete=models.CASCADE)
def __str__(self):
        return self.sterm

