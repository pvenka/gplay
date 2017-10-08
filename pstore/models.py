from django.db import models

# Create your models here.

class QueryResult(models.Model):
  sterm = models.CharField(
	 max_length=255,
	)
  category = models.CharField(
         max_length=255,
	)
  title = models.CharField(
	 max_length=255,
	)
  link = models.CharField(
  	 max_length=255,
	)

def __str__(self):
	return ' '.join([
	  self.category,
	  self.title,
	  self.link,
	])

class App(models.Model):
  sterm = models.CharField(
         max_length=255,
        )
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
