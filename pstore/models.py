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
